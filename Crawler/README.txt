######################################################################################################
####################################        HOMEWORK 1         #######################################
######################################################################################################

 GOAL: Implementing your own web crawler. Performing focused crawling.

 HOMEWORK SUMMARY:

 Task 1: Crawling the documents

		> Perform two crawling rounds 
		     1. Following Breadth First Search Algorithm.
		     2. Following Depth First Search Algorithm.
		> Starting seed : "https://en.wikipedia.org/wiki/Solar_eclipse"
		> Crawling depth : Max = 6.
		> Maximum unique URLS to be crawled = 1000.
		> Generate two files which contain the lists of Unique URLs for each round (BFS and DFS)
		> Download the HTML content of the URL crawled in BFS round.
		> Compare the results obtained from two crawls in terms of URL overlap, perceived quality  
		  and efficiency aspect, coverage of crawl topics(i.e. solar eclipse).
		  
 Task 2: Focused Crawling

		> Perform two one crawling round following Breadth First Search Algorithm.
		> Crawler should take two inputs URL and list of keywords to be matched with anchor text 
		  or the URL
		> KeyWords to be matched : ['lunar', 'moon'].(should handle all variations such as 
		  “Moon_landing”, “Moonlit”,“Lunar”, “honeymoons”, “LUNAR”, etc )
		> Starting seed : "https://en.wikipedia.org/wiki/Solar_eclipse"
		> Crawling depth : Max = 6.
		> Maximum unique URLS to be crawled = 1000.
		> Generate one file which contain the lists of Unique URLs for BFS crawl.
		> Description of the handling of the keyword variations.

#######################################################################################################

 DELIVERABLES:

		> Source Code : FocusedWebCrawler.py, WebCrawler.py
		> README.txt  : Details of the tasks, deliverables, setup or installation guide, steps 
		                to run the program.
		> Three text files : ListOfUrlsBFS.txt, ListOfUrlsDFS.txt, ListOfUrlsFocusedCrawl.txt
		> Text file for task 1 containing detailed explanation: Task1.txt
		> Text file for task 2 containing detailed explanation: Task2.txt
		
#######################################################################################################

 INSTALLATION GUIDE:

		> Download Python 2.7 from : "https://www.python.org/download/releases/2.7/"
		> Set Environment variables for Python [for detailed steps refer : 
		  "https://docs.python.org/2/using/windows.html" ]
		> Install BeautifulSoup and Requests by the following the below steps:
		       1. Open command prompt (cmd) in Windows.
		       2. Run Command : 'pip install BeautifulSoup4'
		       3. After successful installation. 
		       4. Run Command : 'pip install requests'
		       
#######################################################################################################


 STEPS TO RUN PROGRAM:

		> Open Command Prompt in Windows
		> Navigate to the desired directory where the files FocusedWebCrawler.py, WebCrawler.py 
		  are placed.
		> Run the program using the commands: 'python WebCrawler.py' [ for Task 1 ]
		                                      'python FocusedWebCrawler.py' [ for Task 2 ]
		     
########################################################################################################

RESULTS:

		> After running the command 'python WebCrawler.py' 
		  This will lead to creation of two directories and two text files in the same directory:
		     1. BFS-FILES : this contains text files containing HTML content for each crawled URL 
		        using BFS.
		     2. ListOfUrlsBFS.txt : this contains list of 1000 URLS crawled by BFS crawler.
		     3. ListOfUrlsDFS.txt : this contains list of 1000 URLS crawled by DFS crawler.
		     
		> After running the command 'python WebCrawler.py'
		   This will lead to creation of one directory and a text file in the same directory.
		     1. ListOfUrlsFocusedCrawl.txt : this contains list of 1000 URLS crawled by BFS focused 
		        crawler.

