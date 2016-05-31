def compoundSplitter(worddict,morphlist):
        try:
                sorted_wordlist = sorted(worddict.items(), key=operator.itemgetter(1))

                for word in sorted_wordlist:
                    print word[0]
                    for i in range(len(word[0])):
                        for j in range(i+1,min(6,len(word[0]))):
                                if word[0][i:j] in worddict.keys():
                                    print word[0][i:j]
                                    print worddict[word[0][i:j]]
                                    # Compound split algorith goes here
                                    # Previous implementation removed due to issues in code.

        except Exception as e:
                print "\tError %s" % str(e.message)
        return "yay"
