#######################################################################################################
####################################        HOMEWORK 3        #########################################
#######################################################################################################

 GOAL: Implementing your own inverted indexer. Text processing and corpus statistics.

 HOMEWORK SUMMARY:

 Task 1: Generating Corpus

		> A. Parse and tokenize each article from the previously crawled data using BFS algorithm 
		     and generate a text file per article that contains only the title and plain textual 
		     content of the article.Ignore/remove ALL markup notation (HTML tags), URLs, references 
		     to images, tables, formulas, and navigational components. Each text file generated 
		     should correspond to one Wikipedia article and the file name should be same as the 
		     title of the article. The parser should perform both case folding and punctuation 
		     handling.
		  
 Task 2: Implementing an inverted indexer and creating inverted indexes.

		> A. Implement a simple inverted indexer that will consume the corpus generated in Task1 
			 as input and generate an inverted index as ouput.
			 The format of the inverted list : TERM -> (docID,	tf),(docID,	tf),...
			 Whereas TERM -> is defined as a word gram and n=1,2 and 3
			 Therefore constructing three different indexes (unigram, bigram and trigram)
		> B. Store the number of terms in a different data structure.
		> C. Generate another unigram index storing the term position.

 Task 3: Corpus Statistics.
 	  
 	  	> A. For each inverted index generated in previous task, generate a term frequency 
 	  		 table comprising of two columns : term and tf(term frequency). Sort from most to 
 	  		 least frequent.
 	  	> B. For each inverted index generated in previous task, generate a document frequency 
 	  		 table comprising of three columns: term, docIds, and df(document frequency).
 	  	> C. Generate three stop-list, one for each index. Give an explaination on how cut off 
 	  		 value is selected, also comment on the stop-lists' contents.

######################################################################################################

 DELIVERABLES:
 		
 		

		> Source Code       : GenerateCorpus.py (parsing and tokenization) and Indexer.py
		                      (generating index)
		> README.txt        : Details of the tasks, deliverables, setup or installation guide,  
		                      steps to run the program.
		> Four pickle files : Unigram-index.pickle, Bi-gram-index.pickle, Trigram-index.pickle,
							  UnigramPosition-index.pickle containing data structure objects
							  holding of unigram inverted index, bigram inverted index, 
							  trigram inverted index and unigram inverted index with position 
							  of each term respectively. [Explaination of use of pickle in the
							  assignment mentioned below]
		> Four text files   : Unigram-index.txt, Bi-gram-index.txt, Trigram-index.txt, 
							  UnigramPosition-index.txt containing textual format of the
							  unigram inverted index, bigram inverted index, trigram inverted index 
							  and unigram inverted index with position of each term respectively.
		> Three text files  : UnigramTfTable.txt, Bi-gramTfTable.txt, TrigramTfTable.txt containing 
							  the term frequency table for unigram(n=1), bigram(n=2) and trigram(n=3)
							  respectively.
		> Three text files  : UnigramDfTable.txt, Bi-gramDfTable.txt, TrigramDfTable.txt containing 
							  the document frequency table for unigram(n=1), bigram(n=2) and trigram(n=3) 
							  respectively.
		> One text file     : Stoplist.txt containing the stoplist generated from the indexes -unigram, 
							  bigram and trigram and a brief discussion on the cutoff selection and 
							  contents of the stoplist.
		> One text file     : NoTokensPerDoc.txt containing the number of tokens per document in the 
							  corpus.
		> One pickle file   : NoTokensPerDoc.pickle Containing the object of data structure storing the 
							  number of tokens per document.  
		
		Total of 20 files
		
#########################################################################################################

 INSTALLATION GUIDE:

		> Download Python 2.7 from : "https://www.python.org/download/releases/2.7/"
		> Set Environment variables for Python [for detailed steps refer : 
		  "https://docs.python.org/2/using/windows.html" ]
		> Install BeautifulSoup  by the following the below steps:
		       1. Open command prompt (cmd) in Windows.
		       2. Run Command : 'pip install BeautifulSoup4'
		       
##########################################################################################################


 STEPS TO RUN PROGRAM:

		> Open Command Prompt in Windows
		> Keep the documents crawled in earlier tasks in a folder named BFS-FILES 
		> Keep the source code  GenerateCorpus.py and Indexer.py in the same directory in which the 
		  folder BFS-FILES is placed.
		> Now run the program using the commands: 'python GenerateCorpus.py' (To parse, tokenize and  
		  generate files for each article crawled using BFS crawling method ) and wait for the program 
		  to run completely.
		> After successful completion of above program run the program using the commands: 'python 
		  Indexer.py' (To generate index, term frequency table, document frequency tables for 
		  unigrams, bigrams and trigrams)
		     
##########################################################################################################

RESULTS:
        > After running the command 'python GenerateCorpus.py'
          This will automatically generate a folder Corpus containing 1000 files of tokenized and 
          parsed articles
          
		> After running the command 'python Indexer.py' 
		  This will automatically generate 11 text files and 5 pickle files:
		  	Text Files:
		  		1. UnigramTfTable.txt 
		  		2. Bi-gramTfTable.txt
		  		3. TrigramTfTable.txt
		  		4. UnigramDfTable.txt 
		  		5. Bi-gramDfTable.txt
		  		6. TrigramDfTable.txt
		  		7. Unigram-index.txt
		  		8. Bi-gram-index.txt	  
		  		9. Trigram-index.txt
		  		10.UnigramPosition-index.txt
		  		11.NoTokensPerDoc.txt
		  	Pickle Files:
		  		1. Unigram-index.pickle
		  		2. Bi-gram-index.pickle	  
		  		3. Trigram-index.pickle
		  		4. UnigramPosition-index.pickle
		  		5. NoTokensPerDoc.pickle

SPECIAL INSTRUCTIONS:
		
		> Since the deliverables contain pickle files.Here is a brief explanation about pickle.
		  “Pickling” is the process whereby a Python object hierarchy is converted into a byte 
		  stream, and “unpickling” is the inverse operation, whereby a byte stream is converted 
		  back into an object hierarchy.Use of Pickle in this assignment : To easily write 
		  the index onto the disk and load back when required. Pickle helps in reducing the 
		  task(code) of converting the data structure objects to byte stream and vice
          versa.
          
          Note : Refer "https://docs.python.org/2/library/pickle.html" for a detailed explanation 
                 about the pickle module.
                  
DESIGN CHOICES MADE:

		> The index was stored in dictionary data structure having key as terms and value as 
		  another dictionary storing key value pair, key as docID and value as term frequency.
		  {term:{docid:tf}}
		  Use of dictionary to store terms and docIDs helps in fast retrieval.
		> The index storing the term position includes a tuple as value in the second dictionary
		  in below mentioned format
		  {term:{docID:(tf,[pos1,pos2,......]}} 
		> The data structure used for storing the indexes were stored in pickle files for easy 
		  retrieval from disk.
		> Design choices made regarding the stoplist is mentioned in the Stoplist.txt file.
		  	