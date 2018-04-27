############################################################################################################
####################################        HOMEWORK 4        ##############################################
############################################################################################################

 GOAL: Introduction to Lucene. Retrieval and scoring using BM25

 HOMEWORK SUMMARY:

 Task 1: Use Lucene to index corpus and perform retrieval and scoring 

		> A. Use Simple Analyzer of Lucene to index the raw documents of Wikipedia corpus
		> B. Use Lucene's default scoring and ranking functions to perform the search for all the queries 
			 mentioned in ListOfQuery.txt file and return top 100 results for each query. 
		  
 Task 2: Implementing the BM25 ranking algorithm.
 		 
		> A. Implement the BM25 ranking algorithm and write a program to provide a ranked list of 
			 documents for a file with one or more queries. 
		> B. Sort the BM25 scores and return the top 100 results for each query in the file.
		> C. Generate a short report describing the implementation of BM25 ranking algorithm and 
		     discuss the top 5 results between the two search engines for each query.


############################################################################################################

 DELIVERABLES:
 		
 		

		> Source Code      : BM25Ranking.py (BM25 implemenation) and HW4.java (Lucene)
		> README.txt       : Details of the tasks, deliverables, setup or installation guide, steps to run 
		                      the program.
		> Two text files   : Top_100_Query_Result_BM25.txt, Top_100_Query_Result_Lucene.txt storing the top 100
							  results of BM25 ranking algorithm and Lucene respectively for each query.
		> One text file    : ListOfQuery.txt storing the queries
		> One text file    : Imlementation_Report.txt describing the implementation of the ranking algorithm
		> One text file    : Result_Comparison_Report.txt discussing the comparison between the top 5 results of two 
							 search engines.(BM25 and Lucene)
		> Two pickle files : Unigram-index.pickle, NoTokensPerDoc.pickle generated in previous assignments.
		> Two text files   : Unigram-index.txt and NoTokensPerDoc.txt  for reference for the pickle files
							 (Unigram-index.pickle, NoTokensPerDoc.pickle).
		
############################################################################################################	

 INSTALLATION GUIDE:

		> Download Python 2.7 from : "https://www.python.org/download/releases/2.7/"
		> Set Environment variables for Python [for detailed steps refer : 
		  "https://docs.python.org/2/using/windows.html" ]
		> Install BeautifulSoup  by the following the below steps:
		       1. Open command prompt (cmd) in Windows.
		       2. Run Command : 'pip install BeautifulSoup4'
		
		> Download and install the latest JDK and JRE.
		> Set the environment variables.
		> Download the 4.7 version of Lucene from 'https://lucene.apache.org/'
		> Create a new Java Project and the following jars in the build path.
				1. lucene-­core-­VERSION.jar
				2. lucene-­queryparser-­VERSION.jar
				3. lucene-­analyzers-­common-­VERSION.jar
				
		 VERSION - 4.7
		 For further information on version lucene 4.7 goto 'https://archive.apache.org/dist/lucene/java/4.7.2/'
		       
#############################################################################################################


 STEPS TO RUN PROGRAM:

		> Execute the HW4.java by clicking on run and selecting run as java appplication from your IDE.
		> Open the windows power shell, navigate to the directory where ListOfQuery.txt, NoTokensPerDoc.pickle, 
		  Unigram-index.pickle, are placed and run the command python BM25Ranking.py.
		     
#############################################################################################################

RESULTS:
        > After executing the file HW4.java.
          This will automatically generate a file Top_100_Query_Result_Lucene.txt.
          
		> After running the command 'python BM25Ranking.py' 
		  This will automatically generate a file Top_100_Query_Result_BM25.txt.


#############################################################################################################

SPECIAL INSTRUCTIONS:
		
		> Since the deliverables contain pickle files.Here is a brief explanation about pickle.
		  “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and 
		  “unpickling” is the inverse operation, whereby a byte stream is converted back into an object hierarchy.
		  Use of Pickle in this assignment : To easily write the index onto the disk and load back when required. 
          pickle helps in reducing the task(code) of converting the data structure objects to byte stream and vice
          versa.
          
          Note : Refer "https://docs.python.org/2/library/pickle.html" for a detailed explanation about the pickle 
                 module.
                  
#############################################################################################################

CITATIONS AND REFERENCES:

		> https://en.wikipedia.org/wiki/Okapi_BM25 and in-class study materials was referred for BM25 implementation
		> http://lucene.apache.org/ was referred and quoted for Lucene implementation and discussion.