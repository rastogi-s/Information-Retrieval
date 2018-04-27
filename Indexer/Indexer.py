'''
Created on March 15, 2018

@author: shubham rastogi
'''
import glob
import os
import pickle

# corpus directory
DIR_CORPUS='Corpus'

# method to create index
#  TERM:{docId:tf}
def buildIndex(mode):
    invertedList={}
    noOfTokensInDoc={}
    path=os.path.join(DIR_CORPUS,r"*.txt")
    tokenFiles=glob.glob(path)
    for fName in tokenFiles:
        f=open(fName,'r')
        listOfTokens=f.read().split()
        if mode=='bigram':
            listOfTokens=generateBigram(listOfTokens)
        elif mode=='trigram':
            listOfTokens=generateTrigram(listOfTokens)
        docName=fName.split('\\')[1].split('.')[0]
        noOfTokensInDoc[docName]=len(listOfTokens)
        for token in listOfTokens:
            if not token in invertedList:
                invertedList[token]={docName:1}
            else:
                doc=invertedList[token]
                if not docName in doc: 
                    doc[docName]=1
                else:
                    doc[docName]+=1
    
    print "No. of indexed terms: "+str(len(invertedList))
    if mode=='unigram':
        generateNoOfTermsPerDocFile(noOfTokensInDoc);         
    return invertedList
    
def generateBigram(listOfTokens):
    biGramList=[]
    for i in range(1,len(listOfTokens)):
        biGramList+=[listOfTokens[i-1]+" "+listOfTokens[i]]
   
    return biGramList

def generateTrigram(listOfTokens):
    triGramList=[]
    for i in range(2,len(listOfTokens)):
        triGramList+=[listOfTokens[i-2]+" "+listOfTokens[i-1]+" "+listOfTokens[i]]
    
    return triGramList

# create pickle files for each index(unigram, bigram, trigram, unigramWithPos)
def writeIndexToPickleFile(mode,index):
    fName=mode+'-index.pickle'
    if os.path.exists(fName):
        os.remove(fName)
    fileIndex=open(fName,'wb')
    pickle.dump(index,fileIndex)
    fileIndex.close()
  
# create text files for each index(unigram, bigram, trigram)
def writeIndexToTextFile(mode,index):
    fName=mode+'-index.txt'
    if os.path.exists(fName):
        os.remove(fName)
    fileIndex=open(fName,'w')
    fileIndex.write('##########################################################################################\n')
    fileIndex.write('################################ '+ mode +' Inverted Index ##################################\n')
    fileIndex.write('##########################################################################################\n\n\n')
    for term in index:
        fileIndex.write("'"+term+"' : ")
        docDic=index[term]
        s=""
        for doc in docDic:
            s+='('+doc+', '+str(docDic[doc])+'), '
        s=s[:-2]
        fileIndex.write(s+"\n")
    
    fileIndex.close()

# create text file for unigram index with term pos in docs
def writeIndexWithTermPosToFile(mode,index):
    fName=mode+'-index.txt'
    if os.path.exists(fName):
        os.remove(fName)
    fileIndex=open(fName,'w')
    fileIndex.write('##########################################################################################\n')
    fileIndex.write('######################### Unigram Inverted Index with term positions #####################\n')
    fileIndex.write('##########################################################################################\n\n\n')
    for term in index:
        fileIndex.write("'"+term+"' : ")
        docDic=index[term]
        s=""
        for doc in docDic:
            tf,pos=docDic[doc]
            s+='('+doc+', '+str(tf)+', '+str(pos)+'), '
        s=s[:-2]
        fileIndex.write(s+"\n")
        
    
    fileIndex.close()

# method to create index
#  TERM :{docId:(tf,positions)}    
def buildIndexTermPos():
    invertedList={}
    noOfTokensInDoc={}
    path=os.path.join(DIR_CORPUS,r"*.txt")
    tokenFiles=glob.glob(path)
    for fName in tokenFiles:
        f=open(fName,'r')
        listOfTokens=f.read().split()
        docName=fName.split('\\')[1].split('.')[0]
        noOfTokensInDoc[docName]=len(listOfTokens)
        pos=1
        for token in listOfTokens:
            if not token in invertedList:
                invertedList[token]={docName:(1,[pos])}
            else:
                doc=invertedList[token]
                if not docName in doc: 
                    doc[docName]=(1,[pos])
                else:
                    count,p=doc[docName]
                    doc[docName]=(count+1,p+[pos])
            pos+=1
    print "No. of indexed terms: "+str(len(invertedList)) 
    return invertedList
    

def generateTermFreq(index):
    termFreqTable={}
    
    for term in index:
        docDic=index[term]
        count=0
        for doc in docDic:
            count+=docDic[doc]
        termFreqTable[term]=count
    
    sortedTfTable=sorted(termFreqTable.iteritems(),key=lambda(k,v):(v,k),reverse=True)
            
    return sortedTfTable

def writeTfTableToFile(mode,tfTable):
    fName=mode+'TfTable.txt'
    if os.path.exists(fName):
        os.remove(fName)
    fileTf=open(fName,'w')
    fileTf.write('##########################################################################################\n')
    fileTf.write('################################ '+ mode +' Term Frequency Table ############################\n')
    fileTf.write('##########################################################################################\n\n\n')
    fileTf.write('   TERM'+" "*25+'|      TERM FREQUENCY'+'\n')
    fileTf.write('-'*60+'\n')    
    for term,count in tfTable:
        space=" "*(29-len(term))
        fileTf.write("   "+term+space+'|         '+str(count)+'\n')
    fileTf.close()    
    
def generateDocFreq(index):
    docFreqTable=[]
    
    for term in index:
        docDic=index[term]
        count=0
        docStr=""
        for doc in docDic:
            count+=1
            docStr+=doc+", "
        docStr=docStr[:-2]
        docFreqTable+=[(term,docStr,count)]
    
    sortedDfTable=sorted(docFreqTable,key=lambda x:x[0])
            
    return sortedDfTable

def writeDfTableToFile(mode,dfTable):
    fName=mode+'DfTable.txt'
    if os.path.exists(fName):
        os.remove(fName)
    fileTf=open(fName,'w')
    fileTf.write('##########################################################################################\n')
    fileTf.write('################################ '+ mode +' Document Frequency Table ########################\n')
    fileTf.write('##########################################################################################\n\n\n')
    fileTf.write('   TERM'+" "*25+'|      DOC FREQUENCY'+" "*5+'|       DOC IDs'+'\n')
    fileTf.write('-'*80+'\n')    
    for term,docStr,freq in dfTable:
        space1=" "*(29-len(term))
        s=""+str(freq)
        space2=" "*(15-len(s))
        fileTf.write("   "+term+space1+'|         '+str(freq)+space2+'|    '+docStr+'\n')
    fileTf.close()
    
def generateNoOfTermsPerDocFile(noOfTokensPerDoc):
    fName='NoTokensPerDoc.txt'
    if os.path.exists(fName):
        os.remove(fName)
    fileIndex=open(fName,'w')
    fileIndex.write('##########################################################################################\n')
    fileIndex.write('#################################### Tokens Per Document #################################\n')
    fileIndex.write('##########################################################################################\n\n\n')
    for doc in noOfTokensPerDoc:
        fileIndex.write("'"+doc+"':  "+str(noOfTokensPerDoc[doc])+"\n")
    fileIndex.close()
    fName='NoTokensPerDoc.pickle'
    if os.path.exists(fName):
        os.remove(fName)
    fileIndex=open(fName,'wb')
    pickle.dump(noOfTokensPerDoc,fileIndex)
    fileIndex.close()
                
    
    
if __name__=='__main__':
    
    print('Generating Unigram Index.......')
    #unigram
    unigramIndex=buildIndex('unigram')
    writeIndexToPickleFile('Unigram',unigramIndex)
    writeIndexToTextFile('Unigram',unigramIndex) 
    
    print('Generating Bigram Index.......')
    #bigram
    bigramIndex=buildIndex('bigram')
    writeIndexToPickleFile('Bi-gram',bigramIndex)
    writeIndexToTextFile('Bi-gram',bigramIndex)

    print('Generating Trigram Index.......')
    # trigram
    trigramIndex=buildIndex('trigram')
    writeIndexToPickleFile('Trigram',trigramIndex)
    writeIndexToTextFile('Trigram',trigramIndex)

    
    print('Generating Unigram Index with term position in each document.......')
    # unigram
    unigramPosIndex=buildIndexTermPos()
    writeIndexToPickleFile('UnigramPosition',unigramPosIndex)
    writeIndexWithTermPosToFile('UnigramPosition',unigramPosIndex)

    
    print('Generating Term frequency Table.......')
    # unigram
    tfTable=generateTermFreq(unigramIndex)
    writeTfTableToFile('Unigram', tfTable)
    # bigram
    tfTable=generateTermFreq(bigramIndex)
    writeTfTableToFile('Bi-gram', tfTable)
    #trigram
    tfTable=generateTermFreq(trigramIndex)
    writeTfTableToFile('Trigram', tfTable)
    
    print('Generating Document frequency Table.......')
    # unigram
    dfTable=generateDocFreq(unigramIndex)
    writeDfTableToFile('Unigram', dfTable)
    # bigram
    dfTable=generateDocFreq(bigramIndex)
    writeDfTableToFile('Bi-gram', dfTable)
    # trigram
    dfTable=generateDocFreq(trigramIndex)
    writeDfTableToFile('Trigram', dfTable)
    
    # use the following code to load back index onto memory from disk 
#     f=open('unigram-index.pickle')
#     x=pickle.load(f)
#     print(x)