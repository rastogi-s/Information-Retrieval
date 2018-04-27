'''
Created on Feb 20, 2018

@author: shubham rastogi
'''

import requests
import time
import os
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
    outlinkMap={}
    # loop till stack is empty or maximum no. of files has been crawled
    while stack and len(visited_urls)<MAXIMUM_FILES:
        url,depth=stack.pop(-1)
        if depth > MAXIMUM_DEPTH or url in visited_urls:
            continue
        page=requests.get(url)
        text=page.text
        time.sleep(1)
        soupObj=BeautifulSoup(text,'html.parser')
        urlList,allUrlsTitle=fetchUrls(soupObj,visited_urls,depth)
        if urlList==None and allUrlsTitle==None:
            print 'Redirected URL discarded :'+url
            continue
        title=url.split('/')[-1]
        outlinkMap[title]=allUrlsTitle
        urlList.reverse()
        stack+=urlList
        visited_urls.append(url)
        # to keep track of completion of task
        if (len(visited_urls)%50==0):
            print("Crawling using DFS "+str((len(visited_urls)/float(MAXIMUM_FILES))*100)+'% complete')
    global INDEX
    INDEX=1
    return (visited_urls,outlinkMap)

# crawler using bfs approach
def BFS_Crawler():
    visited_urls=[]
    depth=1
    queue=[(SEED,depth)]
    outlinkMap={}
    # loop till stack is empty or maximum no. of files has been crawled or max depth reached
    while queue and len(visited_urls)<MAXIMUM_FILES and depth< MAXIMUM_DEPTH:
        url,depth=queue.pop(0)

        if url in visited_urls:
            continue        
        page=requests.get(url)
        text=page.text
        time.sleep(1)
        soupObj=BeautifulSoup(text,'html.parser')
        urlList,allUrlsTitle=fetchUrls(soupObj,visited_urls,depth)
        if urlList==None and allUrlsTitle==None:
            print 'Redirected URL discarded :'+url
            continue
        title=url.split('/')[-1]
        outlinkMap[title]=allUrlsTitle
        queue+=urlList
        visited_urls.append(url)
        # to keep track of completion of task
        if (len(visited_urls)%50==0):
            print("Crawling using BFS "+str((len(visited_urls)/float(MAXIMUM_FILES))*100)+'% complete')
    global INDEX
    INDEX=1
    return (visited_urls,outlinkMap)
        
        
# fetches all relevant URLS from the current page.
def fetchUrls(soupObj,visited,depth):
    child_urls=[]
    allUrlsTitle=[]
    if soupObj.findAll("span", {"class" : "mw-redirectedfrom" }):
        canonicalLink = soupObj.findAll('link',{'rel':re.compile('canonical') })
        for l in canonicalLink:
            h=l.get('href').encode('utf-8')
            if h in visited: 
                return (None,None)
    
    for dataset in soupObj.findAll('div',{'id':'bodyContent'}):
        for links in dataset.findAll('a',{'href':re.compile('^/wiki/')}):
            href=links.get('href').encode('utf-8')
            if '#' in href:
                href=href[0:href.index('#')]
            if ':' in href or href=='/wiki/Main_Page':
                continue
            if href not in visited: 
                child_urls+=[(BASE_URL+href,depth+1)]
            allUrlsTitle+=[href.split('/')[-1]]
            
    
    return (child_urls,allUrlsTitle)


def createGraph(titleMap,mode,resList2):
    graph={}
    for parent in titleMap:
        for child in titleMap[parent]:
            if child in titleMap.keys():
                if child not in graph:
                    graph[child]=[parent]
                else:
                    if parent not in graph[child]:
                        graph[child].append(parent)
    
    graphFile=open('Graph_'+mode+'.txt','a')
   
    for url in resList2:
        title=url.split('/')[-1]
        graphFile.write(title+" ")
        if title in graph:
            for childTitle in graph[title]:
                graphFile.write(childTitle+" ")
        graphFile.write('\n')
    graphFile.close()
    


if __name__=="__main__":
    
    # deletes existing and creates new files and folder for a fresh execution.
    if os.path.exists('Graph_BFS.txt'):
        os.remove('Graph_BFS.txt')
    if os.path.exists('Graph_DFS.txt'):
        os.remove('Graph_DFS.txt')
    
    print('******** Starting Crawling using DFS *********')
    resList1,titleMapDFS=DFS_Crawler()
    createGraph(titleMapDFS,'DFS',resList1)
    
  
    print('******** Starting Crawling using BFS *********')
    resList2,titleMapBFS=BFS_Crawler()
    createGraph(titleMapBFS,'BFS',resList2)

    