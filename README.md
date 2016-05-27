PROJECT:
--------
Partial(incomplete) implementation of Macherey et. al. Language Independent Compound Splitting Algorithm



Files :
-------
Main.py - Main executable file where the main method is declared
fromPhraseTable.py - Contains the methods for extracting compond parts and morphological operations from phrase tables.
fromMonolingData.py - Contains the methods for extracting word frequency list from monolingual corpus.
compoundSplit.py - Final compound splitter algorithm (incomplete)



Folder :
--------
Data	 - Contains the phrase tables extracted using Moses tool.
		 - Europal corpus german
		 - dummy phrase tables used for testing



Instructions for exection:
--------------------------
python Main.py



Issues:
-------

1. Exponential complexity in extracting morphological operations - fromPhraseTable.py
2. Compound Splitter algorithm incomplete - compoundSplit.py


