#!/usr/bin/python
# -*- coding: utf-8 -*-
from config import settings

def getBetterHeadlines(seoLibrary, siteTokens):
    titleList = [seoDocument.dataDocument.title for seoDocument in seoLibrary.seoDocuments]
    betterHeadlines = getBetterSentences(titleList, siteTokens)
    h1TagsList = []
    if len(betterHeadlines) < settings.BETTER_HEADLINES_LIMIT:
        from nltk.probability import FreqDist
        titlesFreq = FreqDist(titleList)
        for seoDocument in seoLibrary.seoDocuments:
            try:
                if titlesFreq[seoDocument.dataDocument.title] > 1:
                    h1TagsList.extend(seoDocument.dataDocument.h1[0:5])
            except:
                continue
        betterHeadlines.extend(getBetterSentences(list(set(h1TagsList)), siteTokens))
    
    return betterHeadlines

def getBetterSentences(sentences, siteTokens):
    betterSentences = removeExtremeSentences(sentences)
    betterSentences = removeCommonsParts(betterSentences)
    betterSentences = sanitizeSentences(betterSentences)

    betterSentences = _getBetterSentenceWithTokens(betterSentences, siteTokens)
    
    betterSentences = list(set(betterSentences))
    
    return sorted(betterSentences, key=len)[0:settings.BETTER_HEADLINES_LIMIT]

def _getBetterSentenceWithTokens(sentences, tokens):
    betterSentences = []
    
    for title in sentences:
        found = False
        for token, _score in tokens:
            if token in title:
                found = True
                break
        if found:
            betterSentences.append(title)
    
    return betterSentences

def removeExtremeSentences(sentences):
    try:
        sentencesLenList = [len(sentence) for sentence in sentences]
        import numpy as np
        minLen = np.percentile(sentencesLenList,25)
        maxLen = np.percentile(sentencesLenList,90)
        return [sentence for sentence in sentences if len(sentence) >= minLen and len(sentence) <= maxLen]
    except:
        return []
    
def removeCommonsParts(sentences):
    try:
        import operator
        commons = {}
        
        for index, sentence in enumerate(sentences):
            for sentence2compare in sentences[index+1:]:
                if sentence != sentence2compare:
                    commonSubString = longestSubstringFinder(sentence, sentence2compare)
                    if commonSubString and len(commonSubString) > 10:
                        if commonSubString not in commons:
                            commons[commonSubString] = 0
                        commons[commonSubString] += 1
        
        if commons:    
            commons = sorted(commons.items(), key=operator.itemgetter(1), reverse=True)
            commonString = commons[0][0]
            return [sentence.replace(commonString, '') for sentence in sentences]
        
        return sentences
    except:
        return sentences

def sanitizeSentences(sentences):
    sanitizeSentences = []
    for sentence in sentences:
        sentence = sentence.replace('\n', ' ').replace('\r', '').replace('\'', '').replace('"', '')
        if '-' in sentence:
            sentence = longestPart(sentence, '-')
        if '|' in sentence:
            sentence = longestPart(sentence, '|')
        if ':' in sentence:
            sentence = longestPart(sentence, ':')

        sanitizeSentences.append(sentence.strip())
    
    return sanitizeSentences

def longestPart(title, splitter):
    parts = title.split(splitter)
    parts.sort(lambda x,y: len(x) < len(y))
    return parts[0]

def longestSubstringFinder(string1, string2):
    candidates = []
    parts1 = string1.split()
    parts2 = string2.split()
    for index1, part1 in enumerate(parts1):
        for index2, part2 in enumerate(parts2):
            if part1 == part2:
                candidates.append(substring(parts1[index1:], parts2[index2:])) 
    
    if candidates:    
        candidates.sort(key = lambda s: len(s), reverse=True)    
        return candidates[0]
    else:
        return None

def substring(parts1, parts2):
    commonString = []
    for index, part1 in enumerate(parts1):
            try:
                if parts1[index] == parts2[index]:
                    commonString.append(part1)
            except:
                break
    return u' '.join(commonString)

