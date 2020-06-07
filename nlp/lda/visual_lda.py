#!/usr/bin/python
# -*- coding: utf-8 -*-



import jinja2
import random
import json

## numpy array serializable
import numpy as np
from nlp.lda.classifier import findLdaTopicNames

class NumPyArangeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            print('list')
            return obj.tolist() # or map(int, obj)
        elif isinstance(obj, (np.int64, np.int_, np.int32 )):  # windows. https://bugs.python.org/issue24313  64-bit Windows is LLP64.
            return long(obj)
        elif isinstance(obj, np.complex_):  
            return obj.real
        elif isinstance(obj, (np.float64, np.float_, np.float32)):
            return "%.2f" % obj
        print(type(obj))
        return json.JSONEncoder.default(self, obj)

# General HTML template.  This should work correctly whether or not requirejs
# is defined, and whether it's embedded in a notebook or in a standalone
# HTML page.
GENERAL_HTML = jinja2.Template("""
<link rel="stylesheet" type="text/css" href="{{ ldavis_css_url }}">


<div id={{ visid }} class="svg-container"></div>
<script type="text/javascript">

var {{ visid_raw }}_data = {{ vis_json }};

function LDAvis_load_lib(url, callback){
  var s = document.createElement('script');
  s.src = url;
  s.async = true;
  s.onreadystatechange = s.onload = callback;
  s.onerror = function(){console.warn("failed to load library " + url);};
  document.getElementsByTagName("head")[0].appendChild(s);
}

if(typeof(LDAvis) !== "undefined"){
   // already loaded: just create the visualization
   !function(LDAvis){
       new LDAvis("#" + {{ visid }}, {{ visid_raw }}_data);
   }(LDAvis);
}else if(typeof define === "function" && define.amd){
   // require.js is available: use it to load d3/LDAvis
   require.config({paths: {d3: "{{ d3_url[:-3] }}"}});
   require(["d3"], function(d3){
      window.d3 = d3;
      LDAvis_load_lib("{{ ldavis_url }}", function(){
        new LDAvis("#" + {{ visid }}, {{ visid_raw }}_data);
      });
    });
}else{
    // require.js not available: dynamically load d3 & LDAvis
    LDAvis_load_lib("{{ d3_url }}", function(){
         LDAvis_load_lib("{{ ldavis_url }}", function(){
                 new LDAvis("#" + {{ visid }}, {{ visid_raw }}_data);
            })
         });
}
</script>
""")

def generateLdaHtml(seoLibrary, ldaTopics, ldaTopicsTable):
    from api.seo_terms_discovery import _lemma2Token
    
    ldaTopicsTableDict = ldaTopicsTable.to_dict()
        
    for index, _topic in enumerate(ldaTopics):
        lemmaTable =  ldaTopicsTableDict['token.table']['Term']
        tinfoTable =  ldaTopicsTableDict['tinfo']['Term']
        
        tokenTable = _lemma2Token([(token, index) for index,token in enumerate(lemmaTable)], seoLibrary)[0]
        for token, index in tokenTable:
            ldaTopicsTableDict['token.table']['Term'][index] = token
        
        tokenTable = _lemma2Token([(token, index) for index,token in enumerate(tinfoTable)], seoLibrary)[0]
        for token, index in tokenTable:
            ldaTopicsTableDict['tinfo']['Term'][index] = token
    
    
    # get topics categories
    topicsFreq = ldaTopicsTable[0]['Freq'].to_dict()
    topicsCategories = findLdaTopicNames(ldaTopics, topicsFreq, seoLibrary.language, seoLibrary.country)
    
    topicNamesV = []
    for categories in topicsCategories:
        try:
            topicNamesV.append(categories['verticals'][0][0])
        except:
            topicNamesV.append('')
    topicNamesP = []
    for categories in topicsCategories:
        try:
            topicNamesP.append(categories['products'][0][0])
        except:
            topicNamesP.append('')
        
    ldaTopicsTableDict['mdsDat']['topicNamesV'] = topicNamesV
    ldaTopicsTableDict['mdsDat']['topicNamesP'] = topicNamesP 
    
    return prepared_data_to_html(ldaTopicsTableDict)

def prepared_data_to_html(data):

    template = GENERAL_HTML

    d3_url = "https://cdnjs.cloudflare.com/ajax/libs/d3/3.5.5/d3.min.js"
    #ldavis_url = "https://cdn.rawgit.com/bmabey/pyLDAvis/files/ldavis.v1.0.0.js"
    ldavis_url = "http://frontend.seologies.com/js/ldavis.v1.0.0.js"
    #ldavis_css_url = "https://cdn.rawgit.com/bmabey/pyLDAvis/files/ldavis.v1.0.0.css"
    ldavis_css_url = "http://frontend.seologies.com/css/ldavis.v1.0.0.css"

    visid = 'ldavis_' + str(int(random.random() * 1E10))

    return template.render(visid=json.dumps(visid),
                           visid_raw=visid,
                           d3_url=d3_url,
                           ldavis_url=ldavis_url,
                           vis_json=json.dumps(data, cls=NumPyArangeEncoder),
                           ldavis_css_url=ldavis_css_url)