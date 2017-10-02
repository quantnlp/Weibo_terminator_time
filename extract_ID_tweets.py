# -*- coding: utf-8 -*-
"""
Get specific ID data and write to text
Only get text

Created on Sat Sep 30 16:21:15 2017

@author: Frank-Mia
"""
import os
import pickle
import pandas as pd
import re

os.getcwd()
os.chdir("D:\\NLP\\data")


def readWeiboCorpus(pklFile):
    with open(pklFile, 'rb') as f:
        corpusRead = pickle.load(f)
    return corpusRead

def extract(pklFile):        
    #pklFile = 'weibo_content-finance2-20170929.pkl'
    
    corpusRead = readWeiboCorpus(pklFile)  
    
    #ids = sorted(list(corpusRead.keys()))
    for id in corpusRead:
        fileOutName = pklFile.split(".")[0] + "-" + str(id) + ".txt"
        tweets = corpusRead[id]["weibo_content"]
        for i in tweets:
            istr = i 
            istr = i.replace("\u200b","") # remove zero width space
            istr = re.sub(r"http\S+", "", istr) # remove http link in string
            istr = istr.replace("\xa0","") # remove zero width space
            istr = istr.replace("APP下载地址：","") 
            istr = istr.replace("\', \'"," ") 
            istr = istr.replace("\u3000"," ") 
            istr = istr.replace("↓↓↓"," ")
            with open(fileOutName,'a', encoding='utf8') as handleFileOut:
                handleFileOut.write(istr)
        print("\nWritten successfully to file " + fileOutName)
    #
########################
pklFile = "weibo_content-finance1-20170926.pkl"

extract(pklFile)
