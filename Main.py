#!/usr/bin/sh
# -*- coding: utf-8 -*-

import re,datetime,sys,itertools,difflib,operator
import nltk
from nltk.metrics import edit_distance as edit_dist
import fromPhraseTable
import fromMonolingData
import compoundSplit   


if __name__ == '__main__':
	   
	#Read data from phrase table with source to target translation , i.e German to English 
       	source_data = fromPhraseTable.readPhrase('/mount/arbeitsdaten12/users/veluthay/Project1/data/phrase-table-de-en-dummy')
	#Read data from phrase table with target to source translation , i.e English to German
	target_data = fromPhraseTable.readPhrase('/mount/arbeitsdaten12/users/veluthay/Project1/data/phrase-table-en-de-dummy')
	
	#Get compound candidates from the phrase tables.
	print "getting compounds..."
	trans_dict = fromPhraseTable.getCompounds(source_data,target_data)


	print "extracting morphological operations"
	morph_dict = fromPhraseTable.getMorphology(trans_dict)
        #print morph_dict
        #morph_dict = ['-/-','s/-','es/-','n/-','e/-','en/-']
        corpus = fromMonolingData.readFile('/mount/arbeitsdaten12/users/veluthay/Project1/data/europarl-v7.de')
        corpus_1 = fromMonolingData.bootstrap(corpus)
        compoundSplitter(corpus_1,morph_dict)
	print datetime.datetime.now()
	
