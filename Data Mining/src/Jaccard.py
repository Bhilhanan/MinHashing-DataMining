import os
import pickle
import numpy as np
import time
#########################################True Baseline Jaccard Similarity############################
t1=time.time()
inputFile=open("output.txt","r")
documentSet=[]
i=0
for line in inputFile:
    line=str(line).replace("\n", "")
    documentSet.append(set(line.split(" ")))
    i+=1
inputFile.close()

similarityMatrix=[]
i=0
j=0
k=1

fout=open("JaccardBaseTime.txt","w")
for s in documentSet:
    documentIndex=[]
    for s1 in documentSet:
        #documentIndex.append(len((s&s1))*1.0/len(s|s1))
        fout.write(str(round(len(s&s1)*1.0/len(s|s1),4))+" ")
        j+=1
    #similarityMatrix.append(documentIndex)
    fout.write("\n")
    print i
    i+=1

fout.close()
t2=time.time()-t1
print "time taken = "+str(t2)
#########################################################################################################


#
#
# docDict=[]
# i=0
# j=0
# for doc in documentSet:
#     wordDict=[]
#     for w in doc:
#         wordDict[i]=w
#         i+=1
#     docDict[j]=wordDict
#     j+=1


#for x in range(0,16):

#m=1
#for i in similarityMatrix:
 #   print "\t"+str(m)+"\t  ",
  #  m+=1

# k=1
# for i in similarityMatrix:
#     print "\n"
#     print str(k)+"\t"+ str(i)
#     k+=1
#     print "\n"


#################Shingling####################################################
#  #Shingle - ShingleID mapping
# shingleDict = {}
#
#  #Doc - ShingleID mapping
# docShingleDict = {}
#
# count = 0
# files=0
# inFile=open("output.txt","r")
#  #w=inFile.read().split(" ")
#  #print w
# document=[]
# for lines in inFile:
#     lines=str(lines).replace("\n", "")
#     document.append(lines.split(" "))
# inFile.close()
#
# for wordlist in document:
#     temp = set()
#     files+=1
#     f="file"+str(files)
#     for index in range(0,len(wordlist)-2):
#         shingle = wordlist[index] + " " + wordlist[index+1] + " " + wordlist[index+2]
#         if shingle not in shingleDict.iterkeys():
#             shingleDict[shingle] = count
#             count = count + 1
#             print shingle
#             print "\n"
#             #print count
#
#         temp.add(shingleDict[shingle])
#
#
#     docShingleDict[f] = temp
#
#
# print len(shingleDict)
# output = open("docShingleDict.pkl", 'wb')
# pickle.dump(docShingleDict, output)
# output.close()
#####################################################################################################3
