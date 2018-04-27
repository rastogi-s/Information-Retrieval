######################################################################################################
####################################        HOMEWORK 2        ########################################
######################################################################################################

 GOAL: Link Analysis and PageRank Implementation.

 HOMEWORK SUMMARY:

 Task 1: Obtaining directed web graphs.

		> A. Use the previously crawled data using BFS algorithms to construct a graph G1 in the 
		     below format
		     D1	D2	D3	D4
		     D2	D5	D6
             D3	D7	D8
             where D1 is webpage docID and each line in the graph indicates the in-link relationship.
             which means D1 has three incoming links from D2, D3, D4.
        > B. Use the same steps as in A to construct a graph G2 from the previously crawled data 
             using DFS algorithm.
        > 	 Generate a brief report on simple statistics over graphs G1 and G2, the number of 
             pages with no in-links, the number of pages with no out-links(sinks). 
		  
 Task 2: Link Analysis: Implementations

		> A. Implement the PageRank Algorithm.
		> B. Run the Page Rank Algorithm on G1 and G2 until the their PageRank value converge.
		     To test convergence write a code for perplexity calculation of the PageRank 
		     Distribution.
		> C. Use the result of PageRank algorithm over graph G1(BFS) from part B of Task-2
		     as baseline and compare results with below runs of PageRank Algorithms.
			 1. Re-run the PageRank algorithm using a damping factor d	= 0.55. Does that 
			    affect the process and the resulting PageRank with respect to the baseline?
			    Discuss the results.
			 2. Re-run the PageRank	algorithm in Task2-B for exactly 4 iterations. Discuss 
			    the results obtained with respect to the baseline.
			 3. Sort the documents based on their raw in-link count. Compare the top 10 documents
			    in this run to those obtained in Task2-B. Discuss the pros and cons of using the 
			    in-link count as an alternative to PageRank (address at	least 2	pros and 2 cons).

####################################################################################################

 DELIVERABLES:

		> Source Code : PageRank.py(for page rank implementation) and GraphGeneration.py
		               (for graph generation)
		> README.txt  : Details of the tasks, deliverables, setup or installation guide, 
		                steps to run the program.
		> Two text files : Graph_BFS.txt, Graph_DFS.txt containing graphs generated from 
		                   crawled links usinG BFS and DFS as Crawling algorithms.
		> Graph_Statistics.txt: Containing the statistics of the graph G1(BFS) and G2(DFS)
		> Two text files: Perplexity_G1.txt and Perplexity_G2.txt listing the perplexity 
		                  values obtained in each round until convergence from G1(BFS) and 
		                  G2(DFS).
		> Two text files: PageRanking_Top50_(All_Variations)_G1.txt and  
		                  PageRanking_Top50_(All_Variations)_G2.txt listing the DocIDs and
		                  their PageRanking scores of the top 50 pages for both G1(BFS) and 
		                  G2(DFS) graphs and their variation runs as per task-2
		> Two text files: InLinkCount_Top50_G1.txt and  InLinkCount_Top50_G2.txt listing the 
		                  DocIDs and their In-Links counts of the top 50 pages for both G1(BFS)
		                  and G2(DFS) graphs.
		> Task2-C.txt : Detail report on the result obtained from comparison of each PageRanking
		                run.  
		
############################################################################################################	

 INSTALLATION GUIDE:

		> Download Python 2.7 from : "https://www.python.org/download/releases/2.7/"
		> Set Environment variables for Python [for detailed steps refer : 
		  "https://docs.python.org/2/using/windows.html" ]
		> Install BeautifulSoup and Requests by the following the below steps:
		       1. Open command prompt (cmd) in Windows.
		       2. Run Command : 'pip install BeautifulSoup4'
		       3. After successful installation. 
		       4. Run Command : 'pip install requests'
		       
#############################################################################################################


 STEPS TO RUN PROGRAM:

		> Open Command Prompt in Windows
		> Run the program using the commands: 'python GraphGeneration.py' (To crawl and generate G1(BFS) and  
		  G2(DFS) graphs in files Graph_BFS.txt and Graph_DFS.txt
		> Navigate to the desired directory where the files PageRank.py is placed along with the Graph_BFS.txt 
		  and Graph_DFS.txt
		> Run the program using the commands: 'python PageRank.py'
		     
#############################################################################################################

RESULTS:
        > After running the command 'python GraphGeneration.py'
          This will automatically generate two text files
          		1. Graph_BFS.txt
          		2. Graph_DFS.txt 
		> After running the command 'python PageRank.py' 
		  This will automatically generate 6 text files:
		  		1. Perplexity_G1.txt
		  		2. Perplexity_G2.txt
		  		3. PageRanking_Top50_G1.txt
		  		4. PageRanking_Top50_G2.txt
		  		5. InLinkCount_Top50_G1.txt
		  		6. InLinkCount_Top50_G2.txt
		> The Detail statistics of G1 and G2 will be displayed on the console.

