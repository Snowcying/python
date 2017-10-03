# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:49:28 2017

@author: 陈鑫一
"""

count=30

excludes=['the','he','she','i','in','on','that','off','but','and','to','of','you','a','my','it','not','his','this','but','with','for','your','s','me','be','what','so','him','have','d','will']

def processLine(line,wordCounts):
    line=replacePun(line)
    words=line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word]+=1
        else:
            if word not in excludes:
                wordCounts[word]=1

def replacePun(line):
    for ch in line:
        if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            line=line.replace(ch,"  ")
    return line

def main():
    filename=input("enter a filename:").strip()
    infile=open(filename,"r")
    
    wordCounts={}
    for line in infile:
        processLine(line.lower(),wordCounts)
        
    pairs=list(wordCounts.items())
    #print(pairs,"/n")
    items=[[x,y]for(y,x) in pairs]
    items.sort()
   
    for i in range(len(items)-1,len(items)-count-1,-1):
        print(items[i][1]+"\t"+str(items[i][0]))
     
    infile.close()    
        
    
main()