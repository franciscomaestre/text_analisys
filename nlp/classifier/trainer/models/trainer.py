#!/usr/bin/python
# -*- coding: utf-8 -*-

from time import time
from multiprocessing import cpu_count
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
import pickle

from config import settings

SEARCH_BEST_PARAMS = False

def getModelTrained(clf, trainerData, reloadModel=True):
    filename = settings.CLASSIFIER_MODELS_PATH+'/model_%s_%s_%s.pkl' % (trainerData.language, trainerData.country, settings.TRAINER_TREE_TYPE)
    model = None
    if not reloadModel and settings.CACHE:
        try:
            model = pickle.load(open(filename))
        except:
            pass
    if not model:
        model = _trainModel(clf, trainerData)
        with open(filename, 'wb') as fout:
            pickle.dump(model, fout, protocol=pickle.HIGHEST_PROTOCOL)
            
    return model    

def _trainModel(clf, trainerData):

    print('Entrenando ---- %s model Percentage %s' % (str(clf).split('(')[0], settings.TRAINER_DOWNLOAD_PERCENTAGE))
    
    trainedDocuments, testDocuments, trainedTargets, testTargets = train_test_split(trainerData.documentList, trainerData.targetList,  test_size=0.20, random_state=33)
    
    ###############################################################################
    # define a pipeline combining a text feature extractor with a simple
    # classifier
    
    pipeline = Pipeline([
        ('vect', TfidfVectorizer(decode_error='replace', max_df=.5, ngram_range=(1,1), norm='l2', max_features=None, min_df=1, use_idf=True, sublinear_tf=True)),
        ('clf', clf),
    ])
    
    parameters = {
        'vect__max_df': (.50, ),
        'vect__ngram_range': ((1, 1), ),
        'vect__max_features': (None, ),
        'vect__norm': ('l2', ),
        'vect__min_df': (1, ),
        'vect__use_idf': (True, ),
        'vect__sublinear_tf': (True, ),
        'clf__tol': (1e-4,),
        'clf__C': (1, ),
        'clf__dual': (True, ),
        'clf__fit_intercept': (True, ),
        'clf__alpha': (.0001, ),
    }
    
    """
    Stochastic Gradient Descent. SGD:
    Finding a reasonable regularization term \alpha is best done using GridSearchCV, usually in the range 10.0**-np.arange(1,7).
    Empirically, we found that SGD converges after observing approx. 10^6 training samples. Thus, a reasonable first guess for the number of iterations is n_iter = np.ceil(10**6 / n), where n is the size of the training set.
    
    """
    
    parametersCLF = {key:value for key, value in parameters.items() if key.split('__')[1] in clf.get_params().keys()}
    
    parameters = {key:value for key, value in parameters.items() if 'clf__' not in key}
    
    parameters.update(parametersCLF)
    
    trainer = _getTrainer(pipeline, parameters)
    
    if not SEARCH_BEST_PARAMS:
        print 'NO GRID SEARCH'
    else:
        print(u"Performing grid search...")
        print(u"parameters:")
        print (parameters)
        
    print(u"pipeline:", [name for name, _ in pipeline.steps])
    t0 = time()
    model = trainer.fit(trainedDocuments, trainedTargets)
    print(u"done in %0.3fs" % (time() - t0))
    print()
    
    if SEARCH_BEST_PARAMS:
        print(u"Best score: %0.3f" % trainer.best_score_)
        print(u"Best parameters set:")
        bestParameters = trainer.best_estimator_.get_params()
        for paramName in sorted(parameters.keys()):
            print(u"\t%s: %r" % (paramName, bestParameters[paramName]))
        return model.best_estimator_ 
    else:
        return model   

def _getTrainer(pipeline, parameters):
    # find the best parameters for both the feature extraction and the
    # classifier
    
    # cv=3 3 n_folds cross validation
    # iid=False no supone que los datos están igualmente distribuidos y usa la media en cross validation
    if SEARCH_BEST_PARAMS:
        return GridSearchCV(pipeline, parameters, n_jobs=cpu_count()-2, verbose=2, refit=True, cv=2, iid=False)
    else:
        return pipeline

def testTrainModel(model, trainerData):
    
    _trainedDocuments, testDocuments, _trainedTargets, testTargets = train_test_split(trainerData.documentList, trainerData.targetList,  test_size=0.20, random_state=33)
    
    predictions = model.predict(testDocuments)
    print(classification_report(testTargets, predictions, target_names=trainerData.topicList))