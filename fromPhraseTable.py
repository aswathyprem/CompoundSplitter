#!/usr/bin/sh
# -*- coding: utf-8 -*-

import re,datetime,sys,itertools,difflib,operator
import nltk
from nltk.metrics import edit_distance as edit_dist

""""This method reads the phrase tables, removes special characters and saves the values to a list"""
def readPhrase(filename):
        # Read the contents of a file line-by-line and store them into a 'list' called 'file_data'
        print "Reading file: %s" % filename
	print datetime.datetime.now()
        try:
                file_data = []
                f = open(filename,'r')
                for line in f:
			#split the contents of each line by the character '|||'
                	word = line.split('|||')
			#Remove the special characters from the source and target translations 
			for i in range(len(word)):
				if i == 0 or i == 1:
					word[i] =  re.sub('[,!._;:“„?"\'()]', '', word[i])
					word[i] =  re.sub(' - ', ' ' , word[i])
			file_data.append(word)                               
                f.close()
		print "Done reading..."
        except Exception as e:
                print "\tError %s" % str(e.message)
        return file_data


"""This method extracts the compound parts from the phrase table by selecting only those source words which are translated into multiple target words"""
def getCompounds(source_data,target_data):
	#output = open('compound_candidates.txt','w')
	print datetime.datetime.now()
	new_target_data = []
	translations = {}
	trans_dict = {}
	compoundDict = {}
	compoundList =[]
	pattern = re.compile('[0-9/\\)#$&%]')
	
	# From the target_data keep only the words where a single word translates to another single word
	for element in target_data:
		target_words = element[0].split( )
		source_words = element[1].split()
		if len(target_words) == 1 and len(source_words) == 1:
			new_target_data.append(element)

	# For each line in source_data 
	for line in source_data:
		#split the first two columns by space to count the number of words in each column
		source1 = line[0].split( )
		target1 = line[1].split( )
		translations = {}
		# Select only single length source words that translates to multiple target words and exclude words that are not alphabets or hypens 
		if len(source1) == 1 and not pattern.match(str(line[0])) and len(target1) > 1 and not pattern.match(str(line[1])):	
			#For each word in target1,search for translation in new_target_data
			for i in range(len(target1)):
                   		trans_list = []
                        	for term in new_target_data:
					# minimum length of the term set as 5 for filtering	
					if term[0].lower().strip() == target1[i].lower().strip() and len(term[0]) > 3:				
						trans_list.append(term[1].strip())
									
				if trans_list:			
					translations[target1[i]]=list(set(trans_list))	
			
			# Translations are stored in trans_dict for each target word.	
			if translations:	
				trans_dict[source1[0].strip()]=translations
	# Example entry  'Baugenhemigung': {'building': ['baum', 'bauwerk', 'Geb\xc3\xa4ude', 'Bebauung'], 'permit': ['Genehmigung']}		
	return trans_dict



"""This method extracts the morphological operations"""
def getMorphology(trans_dict):
    	listoflist = []
	morphology = []
        # Open file to write the extracted morphological operations
	f = open('morp_operations.txt','w')
	for word in trans_dict:

                # extract the list of list of compounds parts eg : [['baum', 'bauwerk','Geb\xc3\xa4ude', 'Bebauung'], ['Genehmigung']]
        	listoflist = trans_dict[word].values()
    
                #combines the list of list into a single list    
                combList = list(itertools.chain(*listoflist))
            
                #iterate through the list of compound parts
        	for i in range(0, len(combList)+1):

                        #Create all possible combinations of the compound parts
            		for subset in itertools.permutations(combList,i):
                    
                                # select subsets which contain the same number of words as compound parts
                                # eg :  ['baum','bauwerk', 'Genehmigung'] - FALSE
                                # eg :  ['baum','Genehmigung'] - TRUE 
                		if len(subset) == len(listoflist): 
                                        
                                        #concat the eligible compound candidates eg:baumGenehmigung
                                        tempCompound = ''.join(list(subset))
                                        
                                        #Check if the tempcompound and compound have an edit distance less than or equal to 2
                    			if edit_dist(word.lower(),tempCompound.lower(),transpositions=True) <= 2:
                        			
                                                #extract the morphological operations
                        			del_var = []  
                        			insert_var = []                              
                        			for i,s in enumerate(difflib.ndiff(word.lower(), tempCompound.lower())):
                            				if s[0]==' ': continue
                            				elif s[0]=='-':
                                				del_var.append(s[-1])
                            				elif s[0]=='+':
                                				insert_var.append(s[-1])
                        			if not del_var:
                            				del_var = ["-"]
                        			if not insert_var:
                            				insert_var = ["-"]
                        
                        			oper = ''.join(del_var)+"/"+''.join(insert_var)
				                
                                                #Insert only the unique morphological operations into the morphology list
                        			if oper not in morphology:                            
        	                    			morphology.append(oper)
                                                        #write the morphological operations to a file
							f.write(str(oper)+"\n")
    	
	f.close()
	return morphology




