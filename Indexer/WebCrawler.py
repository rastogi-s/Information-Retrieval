'''
Created on Jan 28, 2018

@author: shubham rastogi
'''

import requests
import time
import os
import shutil
import re
from bs4 import BeautifulSoup

SEED="https://en.wikipedia.org/wiki/Solar_eclipse"
BASE_URL="https://en.wikipedia.org"
INDEX=1
MAXIMUM_FILES=1000
MAXIMUM_DEPTH=6


# crawler using dfs approach
def DFS_Crawler():
    visited_urls=[]
    depth=1
    stack=[(SEED,depth)]
    # loop till stack is empty or maximum no. of files has been crawled
    while stack and len(visited_urls)<MAXIMUM_FILES:
        url,depth=stack.pop(-1)
        if depth > MAXIMUM_DEPTH or url in visited_urls:
            continue
        page=requests.get(url)
        text=page.text
        #time.sleep(1)
        soupObj=BeautifulSoup(text,'html.parser')
        urlList=fetchUrls(soupObj,visited_urls,depth)
        if urlList==None :
            print 'Redirected URL discarded :'+url
            continue
        visited_urls.append(url)
        urlList.reverse()
        stack+=urlList
        createFile(soupObj.prettify('utf-8'),url,('DFS',depth))
        # to keep track of completion of task
        if (len(visited_urls)%50==0):
            print("Crawling using DFS "+str((len(visited_urls)/float(MAXIMUM_FILES))*100)+'% complete')
    global INDEX
    INDEX=1
    return visited_urls

# crawler using bfs approach
def BFS_Crawler():
    visited_urls=[]
    depth=1
    queue=[(SEED,depth)]
    # loop till stack is empty or maximum no. of files has been crawled or max depth reached
    while queue and len(visited_urls)<MAXIMUM_FILES and depth< MAXIMUM_DEPTH:
        url,depth=queue.pop(0)
        flag=False
        for u in visited_urls:
            if u.lower()==url.lower():
                flag=True
                break
        if flag:
            continue
        
        page=requests.get(url)
        text=page.text
        #time.sleep(1)
        soupObj=BeautifulSoup(text,'html.parser')
        urlList=fetchUrls(soupObj,visited_urls,depth)
        if urlList==None :
            print 'Redirected URL discarded :'+url
            continue
        visited_urls.append(url)
        queue+=urlList
        createFile(soupObj.prettify('utf-8'),url,('BFS',depth))
        # to keep track of completion of task
        if (len(visited_urls)%50==0):
            print("Crawling using BFS "+str((len(visited_urls)/float(MAXIMUM_FILES))*100)+'% complete')
    global INDEX
    INDEX=1
    return visited_urls
        
        
# fetches all relevant URLS from the current page.
def fetchUrls(soupObj,visited,depth):
    child_urls=[]
    
    
    if soupObj.findAll("span", {"class" : "mw-redirectedfrom" }):
        canonicalLink = soupObj.findAll('link',{'rel':re.compile('canonical') })
        for l in canonicalLink:
            h=l.get('href').encode('utf-8')
            if h in visited: 
                return None
    

    for dataset in soupObj.findAll('div',{'id':'bodyContent'}):
        for links in dataset.findAll('a',{'href':re.compile('^/wiki/')}):
            href=links.get('href').encode('utf-8')
            if '#' in href:
                href=href[0:href.index('#')]
            if ':' not in href and href not in visited:
                child_urls+=[((BASE_URL+href),depth+1)]
    
    return child_urls

# creates or update files with the URLS and html content.
def createFile(text,url,info):
    
    global INDEX
    mode,depth=info
    fName=mode+'-FILES\FILE-'+str(INDEX)+'.txt'
    if mode == 'BFS':
        if not os.path.exists(mode+'-FILES'):
            os.makedirs(mode+'-FILES')
        contentFile=open(fName,'w')
        contentFile.write(url+"\n"+text)
        contentFile.close()
    urlList=open('ListOfUrls'+mode+'.txt','a')
    urlList.write("#"+str(INDEX)+". : "+url+"   [ Found at depth: "+str(depth)+']\n')
    urlList.close()
    INDEX+=1


if __name__=="__main__":
    
    # deletes existing and creates new files and folder for a fresh execution.
    if os.path.exists('ListOfUrlsBFS.txt'):
        os.remove('ListOfUrlsBFS.txt')
    if os.path.exists('ListOfUrlsDFS.txt'):
        os.remove('ListOfUrlsDFS.txt')
    if os.path.exists('BFS-FILES'):
        shutil.rmtree('BFS-FILES')
    
  
    print('******** Starting Crawling using BFS *********')
    startTimeBFS=time.time();
    resList2=BFS_Crawler()
    endTimeBFS=time.time()
    runTimeBFS=abs(startTimeBFS-endTimeBFS);
   

    