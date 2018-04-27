import math
import os
# Global Variables

# set of all pages
PAGES=[]
# set of sink nodes 
SINK_NODES=[]
# set of pages with their in-links
INLINK_PAGES={}
# set of pages with their out-links count
OUTLINK_PAGES={}
# page-rank teleportation factor



# populate pages, out-link pages, in-link pages and sink-nodes
def fetchGraph(fileName):
    graphFile=open(fileName,'r')
    for line in graphFile.readlines():
        docs=line.split()
        INLINK_PAGES[docs[0]]=docs[1:]
        PAGES.append(docs[0])
        for d in range(1,len(docs)):
            if docs[d] in OUTLINK_PAGES:
                OUTLINK_PAGES[docs[d]]+=1
            else:
                OUTLINK_PAGES[docs[d]]=1
    
    for page in PAGES:
        if page not in OUTLINK_PAGES:
            SINK_NODES.append(page)
        

# calculate page-rank
def calculatePageRank(mode,limit):
    currPageRank={}
    newPageRank={}
    noOfPages=len(PAGES)
    perplexityList=[]
    perplexityCurr=0
    for page in PAGES:
        currPageRank[page]=1/float(noOfPages)
    
    count=0
    while count<limit:
        sink=0
        for page in SINK_NODES:
            sink+=currPageRank[page]
        
        for page in PAGES:
            newPageRank[page]=(1-D)/noOfPages
            newPageRank[page]+=(D*sink)/noOfPages
            for qPage in INLINK_PAGES[page]:
                newPageRank[page]+=D*currPageRank[qPage]/OUTLINK_PAGES[qPage]
        
        perplexityNew=calculatePerplexity(newPageRank)
        perplexityList.append(perplexityNew)
        changeInPerplexity=abs(perplexityCurr-perplexityNew)
        
        for page in PAGES:
            currPageRank[page]=newPageRank[page] 
        # to automate limited iteration page ranking algorithm      
        if mode!='Limited':
            if changeInPerplexity<1 :
                count+=1
            else:
                count=0
        else:
            count+=1
            
        perplexityCurr=perplexityNew
    
    return (currPageRank,perplexityList)

# calculate perplexity
def calculatePerplexity(pageRank):
    
    sumOfRank=0
    for page in pageRank:
        sumOfRank+=pageRank[page]*math.log(pageRank[page],2)
    
    return 2**(-1*sumOfRank)

# calculate the number of pages with no in-links:
def calculateNoInlinks():
    count=0
    for page in PAGES:
        if not page in INLINK_PAGES or not INLINK_PAGES[page]:
            count+=1 
    
    return count

# calculate the number of pages with no out-links:
def calculateNoOutlinks():
    return len(SINK_NODES)


# first 50 pages based on their page rank score
def orderPagesOnPageRank(pageRank,graph,sec): 
    rankedPages=sorted(pageRank.iteritems(),key=lambda(k,v):(v,k),reverse=True)
    count=1
    fName='PageRanking_Top50_(All_Variations)_'+graph+'.txt'

    filePagerank=open(fName,'a')
    filePagerank.write('############################################################################################################\n')
    if sec==1:    
        filePagerank.write('############### Top 50 Pages and their Page Rank Score for '+graph+ ' with d=0.85 and till convergence #############\n')
    if sec==2:
        filePagerank.write('############### Top 50 Pages and their Page Rank Score for '+graph+ ' with d=0.55 and till convergence #############\n')
    if sec==3:
        filePagerank.write('######### Top 50 Pages and their Page Rank Score for '+graph+ ' with d=0.85 and limited iterations( only 4) ########\n')
    
    filePagerank.write('############################################################################################################\n\n\n')
    for pages in rankedPages:
        if count<=50:
            filePagerank.write("# "+str(count)+". Doc ID :"+pages[0]+", "+"PageRank :"+str(pages[1])+"\n")
            count+=1
        else:
            break
    filePagerank.write('\n\n')
    filePagerank.close()
        
        
    
# first 50 pages based on their in-link count score
def orderPagesOnInLinkCount(graph):
    inlinkCount={}
    for page in INLINK_PAGES:
            inlinkCount[page]=len(INLINK_PAGES[page])
            
    sortedPages=sorted(inlinkCount.iteritems(),key=lambda(k,v):(v,k),reverse=True)
    count=1
    fName='InLinkCount_Top50_'+graph+'.txt'
    if os.path.exists(fName):
        os.remove(fName)
    fileInLinkCount=open(fName,'w')
    fileInLinkCount.write('############################################################################################################\n')
    fileInLinkCount.write('############################# Top 50 Pages and their In-Link Count Score for '+graph+' ############################\n')
    fileInLinkCount.write('############################################################################################################\n\n\n')    
    for pages in sortedPages:
        if count<=50:
            fileInLinkCount.write("# "+str(count)+". Doc ID :"+pages[0]+", "+"In-Link Count :"+str(pages[1])+"\n")
            count+=1
        else:
            break
    fileInLinkCount.close()
    
# generate a report for perplexity values    
def generatePerplexityReport(perplexityList,graph):
    fName='Perplexity_'+graph+'.txt'
    if os.path.exists(fName):
        os.remove(fName)
    perplexityFile=open(fName,'w')
    perplexityFile.write('############################################################################################################\n')
    perplexityFile.write('##################################### Perplexity values for '+graph+' #############################################\n')
    perplexityFile.write('############################################################################################################\n\n\n')
    count=1
    for val in perplexityList:
        perplexityFile.write("Round "+str(count)+":"+ str(val)+"\n")
        count+=1
    
    perplexityFile.close()

# clear the global variables
def clearFunc():
    global PAGES,SINK_NODES,INLINK_PAGES,OUTLINK_PAGES
    del PAGES[:]
    del SINK_NODES[:]
    INLINK_PAGES.clear()
    OUTLINK_PAGES.clear()
    
        

# main function
if __name__=='__main__':
    global D
    if os.path.exists('PageRanking_Top50_(All_Variations)_G1.txt'):
        os.remove('PageRanking_Top50_(All_Variations)_G1.txt')
    if os.path.exists('PageRanking_Top50_(All_Variations)_G2.txt'):
        os.remove('PageRanking_Top50_(All_Variations)_G2.txt')
    D= 0.85
    fetchGraph('Graph_BFS.txt')
    print('**************Statistics for BFS-GRAPH(G1)*****************\n')
    print('Number of pages with no in-links  (G1): '+str(calculateNoInlinks()))
    print('Number of pages with no out-links (G1): '+str(calculateNoOutlinks())+'\n')
    pageRankBFS,perplexityListBFS=calculatePageRank('Normal',4)
    generatePerplexityReport(perplexityListBFS, 'G1')
    orderPagesOnPageRank(pageRankBFS,'G1',1)
    orderPagesOnInLinkCount('G1')
    clearFunc()
    fetchGraph('Graph_DFS.txt')
    print('**************Statistics for DFS-GRAPH(G2)*****************\n')
    print('Number of pages with no in-links  (G2): '+str(calculateNoInlinks()))
    print('Number of pages with no out-links (G2): '+str(calculateNoOutlinks())+'\n')
    pageRankDFS,perplexityListDFS=calculatePageRank('Normal',4)
    generatePerplexityReport(perplexityListDFS, 'G2')
    orderPagesOnPageRank(pageRankDFS,'G2',1)
    orderPagesOnInLinkCount('G2')
    clearFunc()
    print('**************Task 2-C (A) *****************\n')
    D=0.55
    fetchGraph('Graph_BFS.txt')
    newPageRankBFS,newPerplexityList=calculatePageRank('Normal',4)
    orderPagesOnPageRank(newPageRankBFS,'G1',2)
    sortedPageRankOld=sorted(pageRankBFS.iteritems(),key=lambda(k,v):(v,k),reverse=True)
    sortedPageRankNew=sorted(newPageRankBFS.iteritems(),key=lambda(k,v):(v,k),reverse=True)
    counter=0
    for i in range(0,len(sortedPageRankOld)):
        if sortedPageRankOld[i][0]!=sortedPageRankNew[i][0]:
            counter+=1
    print('Change in ranking due to change in teleportation factor : '+str(counter))
    print('\nPerplexity values for each round :\n')
    for i in range(0,len(newPerplexityList)):
        print('Round '+str(i+1)+'. '+str(newPerplexityList[i]))
    print('\n**************Top 10 from baseline and  new run of page rank with d=0.55 *****************\n')
    for i in range(0,11):
        print(sortedPageRankOld[i],sortedPageRankNew[i])
    clearFunc()
    fetchGraph('Graph_DFS.txt')
    newPageRankDFS,newPerplexityList=calculatePageRank('Normal',4)
    orderPagesOnPageRank(newPageRankDFS,'G2',2)
    clearFunc()
    print('**************Task 2-C (B) *****************\n')
    D=0.85
    fetchGraph('Graph_BFS.txt')
    newPageRankBFS,newPerplexityList=calculatePageRank('Limited',4)
    orderPagesOnPageRank(newPageRankBFS,'G1',3)
    sortedPageRankNew=sorted(newPageRankBFS.iteritems(),key=lambda(k,v):(v,k),reverse=True)
    counter=0
    for i in range(0,len(sortedPageRankOld)):
        if sortedPageRankOld[i][0]!=sortedPageRankNew[i][0]:
            counter+=1
    print('Change in ranking due to limited iteration : '+str(counter))
    clearFunc()
    fetchGraph('Graph_DFS.txt')
    newPageRankDFS,newPerplexityList=calculatePageRank('Normal',4)
    orderPagesOnPageRank(newPageRankDFS,'G2',3)    