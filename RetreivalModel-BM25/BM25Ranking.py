import math
import os
import pickle


# file name which contains list of queries
LIST_OF_QUERY_FILE_NAME='ListOfQuery.txt'
# output file name storing the top 100 results of BM25 score for all queries 
TOP_100_RESULT_BM25='Top_100_Query_Result_BM25.txt'
# pickle file of inverted index 
UNIGRAM_INVERTED_INDEX_PICKLE_FILE='Unigram-index.pickle'
# pickle file of number of tokens per document in corpus
NUM_OF_TOKEN_PER_DOC_PICKLE_FILE='NoTokensPerDoc.pickle' 
# Query Counter
QUERY_COUNTER=1

# calculate BM25 score of each doc that has the query term
# input : inverted index of uingram, query term frequency dic
# output : a dictionary of docids storing the score in decreasing order
def calculateBM25Score(invertedIndex,queryTermFreq,noOfTokenPerDoc):
    docScore={}
    # no relevance info
    r,R = (0,0)
    # parameters value set empirically
    k1, k2, b = (1.2,100,0.75)
    # Total number of document in the corpus
    N = len(noOfTokenPerDoc)
    # Average document length
    avgDocLen = sum([ noOfTokenPerDoc[doc] for doc in noOfTokenPerDoc])/len(noOfTokenPerDoc)
    
    for qTerm in queryTermFreq:
        # fetch inverted list for the query term if it exists in the index
        if qTerm in invertedIndex:
            invertedList=invertedIndex[qTerm]
        else:
            continue
        # document length
        docLength=noOfTokenPerDoc[doc]
        # the number of documents in which qTerm occurs
        n = len(invertedList)
        # K : one of the parameters
        K = k1*((1-b) + b*(docLength)/float(avgDocLen)) 
        # quert term frequency
        qf=queryTermFreq[qTerm]
        for doc in invertedList:
            # the number of times qTerm occur in the current doc
            f = invertedList[doc]
            param1 = math.log( ((r+0.5)/(R-r+0.5)) / ((n-r+0.5)/(N-n-R+r+0.5)))
            param2 = ((k1 + 1)* f)/(K+f)
            param3=  ((k2 + 1)* qf)/(k2+qf)
            score=param1*param2*param3
            if doc in docScore:
                docScore[doc]+=score
            else:
                docScore[doc]=score     
           
    return docScore

# generate the term frequency of each query term.
# input : query
# output : a dictionary of all terms and their frequency
def generateQueryTermsFreqDict(query):
    queryTermFreq={}
    for qTerm in query.split():
        if qTerm in queryTermFreq:
            queryTermFreq[qTerm]+=1
        else:
            queryTermFreq[qTerm]=1
    
    return queryTermFreq

# fetch the inverted index of unigram from the pickle file
# generated in previous assignment
# output : inverted index of the unigrams
def fetchInvertedIndex():
    f=open(UNIGRAM_INVERTED_INDEX_PICKLE_FILE)
    invertedIndex=pickle.load(f)
    
    return invertedIndex

# fetch the number of tokens per document from the pickle file
# generated in previous assignment
# output : number of tokens per document 
def fetchNoOfTokensPerDocDic():
    f=open(NUM_OF_TOKEN_PER_DOC_PICKLE_FILE)
    noOfTokensPerDoc=pickle.load(f)
    
    return noOfTokensPerDoc

# write the result (BM25 score for the given query
def writeResultToFile(docScore,query):
    global QUERY_COUNTER
    fileBM25=open(TOP_100_RESULT_BM25,'a')
    fileBM25.write("\nQuery Q"+str(QUERY_COUNTER)+": "+query+"\n")
    sortedDocScore=sorted(docScore.iteritems(),key=lambda(k,v):(v,k),reverse=True)
    count=0
    for doc,score in sortedDocScore:
        fileBM25.write(str(QUERY_COUNTER)+" Q0 "+doc +" "+str(count + 1) + " " + str(score) + " BM25\n") 
        count+=1
        if count+1 > 100:
            break  
    QUERY_COUNTER+=1
    fileBM25.close()


if __name__=='__main__':
    if os.path.exists(TOP_100_RESULT_BM25):
        os.remove(TOP_100_RESULT_BM25)
    f=open(LIST_OF_QUERY_FILE_NAME,'r')
    if os.path.exists(TOP_100_RESULT_BM25):
        os.remove(TOP_100_RESULT_BM25)
    fileBM25=open(TOP_100_RESULT_BM25,'a')
    fileBM25.write("##########################################################################################\n"+\
                   "############################# Top 100 Query Results Using BM25 ###########################\n"+\
                   "##########################################################################################\n\n")
    fileBM25.close()
    print "Loading inverted index from pickle file...."
    invertedIndex=fetchInvertedIndex()
    print "Loading number of tokens per document from pickle file...."
    noOfTokenPerDoc=fetchNoOfTokensPerDocDic()
    for query in f.readlines():
        print "\nQuery --> "+ query
        print "Generating query term frequency...."
        queryTermFreq=generateQueryTermsFreqDict(query)
        print "Calculating BM25 score for documents for the current query...."
        docScore=calculateBM25Score(invertedIndex,queryTermFreq,noOfTokenPerDoc)
        print "Writing the top 100 results in the file...."
        writeResultToFile(docScore,query)