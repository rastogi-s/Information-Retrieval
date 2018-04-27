'''
Created on Jan 28, 2018

@author: shubham rastogi
'''
import requests
import time
import os
#import shutil
import re
from bs4 import BeautifulSoup

SEED="https://en.wikipedia.org/wiki/Solar_eclipse"
BASE_URL="https://en.wikipedia.org"
INDEX=1
MAXIMUM_FILES=1000
MAXIMUM_DEPTH=6
KEY_WORD=['lunar','moon']

# crawler using bfs approach
def BFS_Focused_Crawler():
    visited_urls=[]
    depth=1
    queue=[(SEED,depth)]
    while queue and len(visited_urls)<MAXIMUM_FILES and depth< MAXIMUM_DEPTH:
        url,depth=queue.pop(0)
        if url in visited_urls:
            continue
        visited_urls.append(url)
        page=requests.get(url)
        text=page.text
        time.sleep(1)
        soupObj=BeautifulSoup(text,'html.parser')
        queue+=fetchUrls(soupObj,visited_urls,depth)
        createFile(soupObj.prettify('utf-8'),url,depth)
        if (len(visited_urls)%50==0):
            print("Focused Crawling using BFS "+str((len(visited_urls)/float(MAXIMUM_FILES))*100)+'% complete')
    global INDEX
    INDEX=1
    return visited_urls
        
        
# fetch relevant URLS from the current page
def fetchUrls(soupObj,visited,depth):
    child_urls=[]
    for dataset in soupObj.findAll('div',{'id':'bodyContent'}):
        for links in dataset.findAll('a',{'href':re.compile('^/wiki/')}):
            href=links.get('href').encode('utf-8')
            encodedHREF,anchorText=("","")
            
            # removes same file reference from href
            if '#' in href:
                href=href[0:href.index('#')]
            
            # convert the href and anchor text to lower case    
            if href!=None:
                encodedHREF=href.lower()
            if links.text!=None:
                anchorText=links.text.encode('utf-8').lower()

            # check whether the keywords in the href and anchor text exists.  
            flag=False
            for key in KEY_WORD:
                if key in anchorText or key in encodedHREF:
                    flag=True
            # filters duplicate and administrative URLS.
            if ':' not in href and href not in visited and flag:            
                child_urls+=[((BASE_URL+href),depth+1)]
    
    return child_urls

# creates or update files with the URLS.
def createFile(text,url,info):
    
    global INDEX
    depth=info
    #fName='FOCUSED-CRAWL-FILES/FILE-'+str(INDEX)+'.txt'
    #if not os.path.exists('FOCUSED-CRAWL-FILES'):
        #os.makedirs('FOCUSED-CRAWL-FILES')
    #contentFile=open(fName,'w')
    #contentFile.write(text)
    #contentFile.close()
    urlList=open('ListOfUrlsFocusedCrawl.txt','a')
    urlList.write("#"+str(INDEX)+": "+url+"[ Found at depth: "+str(depth)+']\n')
    urlList.close()
    INDEX+=1


if __name__=="__main__":
    if os.path.exists('ListOfUrlsFocusedCrawl.txt'):
        os.remove('ListOfUrlsFocusedCrawl.txt')
    #if os.path.exists('FOCUSED-CRAWL-FILES'):
        #shutil.rmtree('FOCUSED-CRAWL-FILES')
    print('******** Starting Focused Crawling using BFS *********')
    t1=time.time();
    res=BFS_Focused_Crawler()
    t1=abs(t1-time.time());
    print('Execution time for Focused BFS Crawl : '+str(t1) + ' seconds')