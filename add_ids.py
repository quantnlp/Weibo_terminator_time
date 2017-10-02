# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 14:26:41 2017

@author: Frank-Mia
"""

import os
import pickle
import pandas as pd
import re
import codecs

os.getcwd()
os.chdir("D:\\NLP\\weibo_terminator_workflow")

def addIDlist(pklFile, keyName, list2add):
    with open(pklFile, 'rb') as f:
        data = pickle.load(f)
    output = open(pklFile, 'wb')
    data[keyName] = list2add
    pickle.dump(data, output)
    output.close()

def loadFinancialID(n):
    inDir = "D:/NLP/"
    fileFinancialID = "weibo_financal_ID.xlsx"
    IDs = pd.read_excel(inDir + fileFinancialID, "Sheet"+str(n)) 
    return list(IDs.ID)

#############
def readWeiboCorpus(pklFile):
    with open(pklFile, 'rb') as f:
        corpusRead = pickle.load(f)
    return corpusRead
        
def numberTweetsAll(corpusRead):
    numberTweets = 0
    for iid in corpusRead:
        print(iid)
        numberTweets += len(corpusRead[iid]["weibo_content"])
    return numberTweets

pklFile = 'distribute_ids.pkl'
SheetNumber = 4
list2add=loadFinancialID(SheetNumber) # load ID from excel file
#list2add = ["tonghuashun"]
keyName = "finance"+str(SheetNumber)
addIDlist(pklFile, keyName, list2add) # add to distribute id pkl

#COOKIES_SAVE_PATH = 'settings/cookies.pkl'
#with open(COOKIES_SAVE_PATH, 'rb') as f:
#    cookies_dict = pickle.load(f)
##########################################################################
## for analysis
#pklFile = 'D:/NLP/weibo_corpus/weibo_content.pkl'
pklFile = 'D:/NLP/weibo_corpus/weibo_content-finance3-20170929.pkl'
corpusRead = readWeiboCorpus(pklFile)  
numberTweets = numberTweetsAll(corpusRead)
print("Currently has " + str(numberTweets) + " tweets")
ids = sorted(list(corpusRead.keys()))

for id in corpusRead:
    print(id)
    print(corpusRead[id]["weibo_time"][0])
    print(corpusRead[id]["weibo_time"][-1])
    print("*"*20)

## get scaped IDs
#scrapedFile = 'D:/NLP/weibo_terminator_workflow/settings/scraped.mark'
#with open(scrapedFile, 'rb') as f:
#    data = pickle.load(f)

sorted(list(set(data)))
# write tonghuashun to text file
pklFile = 'D:/NLP/weibo_corpus/weibo_content_test.pkl'
corpusRead = readWeiboCorpus(pklFile)
id = "tonghuashun"
tweets = corpusRead[id]["weibo_content"]

tweetList = []
for i in tweets:
    istr = i 
    istr = i.replace("\u200b","") # remove zero width space
    istr = re.sub(r"http\S+", "", istr) # remove http link in string
    istr = istr.replace("\xa0","") # remove zero width space
    istr = istr.replace("APP下载地址：","") 
    istr = istr.replace("\', \'"," ") 
    istr = istr.replace("\u3000"," ") 
    istr = istr.replace("↓↓↓"," ")
    tweetList.append(istr)

with open("tonghuashun-20170929-2.txt", "w", encoding='utf8') as output:
    output.write(str(tweetList))
    
################################ mischellous
# get one tweet: user ID, "weibo_content", i
    id = "ncby"
    N = len(corpusRead[id]["weibo_content"])
#    for i in range(0,110):
    for i in range(N-50,N):
        print(corpusRead[id]["weibo_time"][i] + corpusRead[id]["weibo_content"][i])
    
    badIDs = []
    for id in corpusRead:
#        print(id)
        numberContent = len(corpusRead[id]["weibo_content"])
        numberTime = len(corpusRead[id]["weibo_time"])
        if numberContent!=numberTime:
            badIDs.append(id)
            print(id + ": " + str(numberContent) +", " + str(numberTime))
    
    for id in badIDs:
        corpusRead.pop(id, None)
        
    with open(pklFile, 'wb') as f:
        pickle.dump(corpusRead,f)