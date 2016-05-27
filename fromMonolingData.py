#!/usr/bin/sh
# -*- coding: utf-8 -*-

import re,datetime,sys,itertools,difflib,operator
import nltk
from nltk.metrics import edit_distance as edit_dist



""""This method reads data from a monolingual corpus, remove special characters and saves the words into a list"""
def readFile(filename):
        # Read the contents of a file line-by-line and store them into a 'list' called 'file_data'
        print "Reading file: %s" % filename
        try:
                file_data = []
                f = open(filename,'r')
                for line in f:
                        line = re.sub('[,!.;:“„?"\'()]', '', line)
                        for word in line.split( ):
                                file_data.append(word)
                f.close()
        except Exception as e:
                print "\tError %s" % str(e.message)
        return file_data


"""This method removes non words using pattern matching, computes the frequency of words and creates a dictionary of words with frequency"""
"""It also ignores words with frequncy less than 2  and length of words less than 4 (to be modified for optimization)"""
def bootstrap(corpus):
        try :
                pattern = re.compile('[0-9/\\)#$]')
                pass1 = {}
                for word in corpus:
                        if not pattern.match(word):
                                if word not in pass1:
                                        pass1[word] = 1
                                else :
                                        pass1[word] +=1
                f = open('words.txt','w')
                for key in pass1.keys():
                        if pass1[key] <= 2 or len(key) <=4:
                                del pass1[key]
                        else:
                                f.write(key + ' ' +str(pass1[key]) + '\n')
        except Exception as e:
                print "\tError %s" % str(e.message)
        #sorted_pass1 = sorted(pass1.items(), key=operator.itemgetter(1))
        return pass1
        

	
