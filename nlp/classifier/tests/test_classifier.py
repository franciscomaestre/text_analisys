#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from config import settings
from nlp.classifier.classifier_factory import ClassifierFactory


class ClassifierTest(unittest.TestCase):

    def testWarmUp(self):
        ClassifierFactory.warmUp()
        self.assertTrue(u'es-ES' in ClassifierFactory.MODELS, u'No se ha cargado el modelo es-ES')

    def testSpanishClassifier(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSpanishClassifier']
    unittest.main()