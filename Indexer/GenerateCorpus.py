'''
Created on March 15, 2018

@author: shubham rastogi
'''

import glob
import os
import shutil
import re
import string
from bs4 import BeautifulSoup

DIR_RAW_HTML='BFS-FILES'
DIR_CORPUS='Corpus'


# method to convert HTML content into plain text
# Given: HTML content
# Returns: plain text
def parseHTML(htmlContent):
    soup = BeautifulSoup(htmlContent, 'html.parser')
    divs = soup.findAll('div', {'id':'mw-content-text'})
    
    # remove content below the See_also
    element=soup.find('span',{'id':'See_also'})
    if element and element.find_parent() and not element.find_parent() in divs :
        for siblings in element.find_parent().find_next_siblings():
            siblings.decompose()
        element.find_parent().decompose()
    
    # remove content below the Notes
    element=soup.find('span',{'id':'Notes'})
    if element and element.find_parent() and not element.find_parent() in divs :
        for siblings in element.find_parent().find_next_siblings():
            siblings.decompose()
        element.find_parent().decompose()
     
    # remove content below the References
    element=soup.find('span',{'id':'References'})
    if element and element.find_parent() and not element.find_parent() in divs :
        for siblings in element.find_parent().find_next_siblings():
            siblings.decompose()
        element.find_parent().decompose()
    
    # remove images tags and their captions 
    imgDivList=soup.findAll('div', {'class':'thumb tright'})+soup.findAll('div', {'class':'thumb tleft'})
    for img in imgDivList:
        img.decompose()
    
    # remove any remaining image tags
    for img in soup.findAll('img'):
        img.decompose()   
        
    # remove all formulas 
    for mathItems in soup.findAll('math'):
        mathItems.decompose()    
    
    # remove all tables and their content
    for table in soup.findAll('table'):
        table.decompose()
        
    # remove content navigation
    for conNav in soup.findAll('div', {'id':'toc'}):
        conNav.decompose()
    
    # remove script
    for scripts in soup.findAll('script'):
        scripts.decompose()

    soup.prettify('utf-8', 'html')
    title=soup.find('title').get_text().encode('utf-8')
    header=soup.find('h1').get_text().encode('utf-8')
    body = ''
    for d in divs:
        divText=d.get_text().encode('utf-8')
        # removes all the URLS that are embedded in the text
        divText=re.sub(r'(?<=\W)http\S*','' ,divText)
        body+= divText

    
    return title+header+body


# method to case-fold the text provided
# Given: plain text
# Return: case folded plain text  
def caseFold(plainText):
    return plainText.lower()


# method to remove punctuation from the text provided
# Given: plain text
# Return:  plain text with removed punctuation
def removePunctuation(tokens):
    newList=[]
    for tok in tokens:
        tok=tok.strip(string.punctuation)
        matchNum=re.compile(r'^[\-]?[0-9]*\.?[0-9]+$')
        if not matchNum.match(tok):
            tok=re.sub(r'[^a-zA-Z0-9\--]','',tok)
            tok=tok.strip(string.punctuation)
        newList.append(tok)
        
    return newList
    
    
# method to generate tokens from plain text
# Given: plain text
# Return: list of tokens     
def generateTokens(plainText):
    return list(filter(re.compile('[a-zA-Z0-9_]').search,plainText.split()))


def parser(fileName):
    f = open(fileName, 'r')
    docName = f.readline().split('/')[-1] + '.txt'
    docName=re.sub(r'[^a-zA-Z0-9\_.]','',docName).strip(string.punctuation)
    content = f.read()
    f.close()
    plainText=parseHTML(content)
    caseFoldedPlainText=caseFold(plainText)
    tokens=generateTokens(caseFoldedPlainText)
    tokens=removePunctuation(tokens)
    joinTokens=" ".join(tokens)
    if not os.path.exists('Corpus'):
        os.makedirs('Corpus')
    if os.path.exists('Corpus/'+docName):
        print 'same name file exists' ,'Corpus/'+docName 
    tokenFile=open('Corpus/'+docName,'w')
    tokenFile.write(joinTokens)
    tokenFile.close()
    

if __name__ == '__main__':
    if os.path.exists(DIR_CORPUS):
        shutil.rmtree(DIR_CORPUS)
    path=os.path.join(DIR_RAW_HTML,r"*.txt")
    rawFiles=glob.glob(path)
    i=1
    print "Starting to generate corpus....."
    print "Parsing and Tokenization 0% complete"
    for fileName in rawFiles:
        parser(fileName)
        if i%50==0:
            print("Parsing and Tokenization "+str(i/float(1000)*100)+'% complete')
        i+=1