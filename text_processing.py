import csv
import pandas as pd
import os
import glob
from nltk import tokenize, re
import sys
import string

# write each thread into a line, and merge all files into one file
path = './send/breast cancer.txt'
files = glob.glob(path)
resultList = []
for fileName in files:
    with open(fileName) as data:
        sentences = data.read().splitlines()

    tempStr = ""
    for i in range(0, len(sentences)-1):
        if "Content:" in sentences[i]:
            tempStr += sentences[i+1]
        if "User0:" in sentences[i+1]:
            resultList.append(tempStr)
            tempStr = ""
    resultList.append(tempStr)

f = open('./send/breast cancer1.txt', 'w')
f.writelines(["%s\n" % result for result in resultList])
print "Done"

# with open('./dataset/chv_adr_185.csv','rb') as f:
#     reader = csv.reader(f)
#     adrLists = list(reader)
#
# with open('./dataset/list_disease.csv','rb') as f:
#     reader = csv.reader(f)
#     dLists = list(reader)
#
# with open('./dataset/list_drug.csv','rb') as f:
#     reader = csv.reader(f)
#     rLists = list(reader)
#
# fileName = './dataset/medhelp_drug_all.txt'
# f = open(fileName, 'r+')
# data = f.read()
#
# # preprocess corpus (e.g. to lower case)
# # replace adrs with adr_id, replace disease and drug with disease_emb and drug_emb
# data = data.lower()
# for row in adrLists:
#     for item in row[1:]:
#         if not item:
#             break
#         if item in data:
#             data = re.sub(item, row[0], data)
#             print item, row[0]
#
# for row in dLists[1:]:
#     data = re.sub(row[0], row[1], data)
#     print row[0], row[1]
#
# for row in rLists[1:]:
#     data = re.sub(row[0], row[1], data)
#
# f.seek(0)
# f.write(data)
# f.truncate()
# f.close()

# # ## split text into sentence by sentence, using NLTK
# # open input file, read all columns, address unexpected letters
# fp = open("./data/disease_files_1/all.txt")
# data = fp.read().lower()
# data = unicode(data, errors='ignore')
#
# # tokenize text into sentences, using nltk
# sentences = tokenize.sent_tokenize(data)
#
# # write generated list of strings into txt file
# file = open('./data/all_for_corpus.txt', 'w')
# file.writelines(["%s\n" % sentence for sentence in sentences])
# print 'Done'

# ## process chv file:each row represent an adr, row[0] denotes UMLS id
# data = pd.read_csv("./data/chv.csv")
# ids = data['umls_id'].values
# userTerms = data['user_pre'].values
# chvTerms = data['chv_pre'].values
# umlsTerms = data['umls_pre'].values
# freqs = data['freq'].values
#
# resultLists = []
# currentId = ids[0]
# for i in range(0,len(ids)):
#     if i == 0:
#         resultList = []
#         resultList.append(ids[i])
#         resultList.append(userTerms[i])
#         resultList.append(chvTerms[i])
#         resultList.append(umlsTerms[i])
#         resultList.append(freqs[i])
#     elif ids[i] == ids[i-1]:
#         resultList.append(userTerms[i])
#         resultList.append(chvTerms[i])
#         resultList.append(umlsTerms[i])
#     else:
#         resultLists.append(resultList)
#         resultList = []
#         resultList.append(ids[i])
#         resultList.append(userTerms[i])
#         resultList.append(chvTerms[i])
#         resultList.append(umlsTerms[i])
#         resultList.append(freqs[i])
#
# resultLists.append(resultList)

# # make sure no duplicates in each line, by using set()
# finalLists = []
# for line in resultLists:
#     listToSet = set()
#     result = []
#     for item in line:
#         if item not in listToSet:
#             listToSet.add(item)
#             result.append(item)
#     finalLists.append(result)
#
# with open('./data/chv_processed_1.csv', "wb") as f:
#     writer = csv.writer(f)
#     writer.writerows(finalLists)
# print "Done"

# data = pd.read_csv("./data/list_adrs.csv")
# adrs = data['adr'].values

# with open('./data/chv_processed_11.csv', "wb") as f:
#     writer = csv.writer(f)
#     writer.writerows(outputLists)
# print "Done"








