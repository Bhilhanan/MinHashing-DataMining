import os
import time
from math import sqrt

mseFile=open("mse.txt","w")
jaccardFile=open("JaccardBase.txt","r")
minHashFile=open("similarity_matrix_128.txt","r")

k=11519
i=0
j=[]
m=[]
mse=[0.0]*k
a=0
b=[]
while(k>=0):
    j=str(jaccardFile.readline()).split()
    #print j
    m=str(minHashFile.readline()).split()
    #print m
#     diff=len(m)-len(j)
#     if(diff!=0):
#         print str(len(j))+" "+str(len(m))
    try:     
        for x in range(k):
            s=((float(m[x])-float(j[x])))*1.0
            a+= s*s
            #i+=1
        #mse[i]=mse[i]*1.0/k
        #i+=1
        #print i
        k=k-1
    except IndexError as err:
        break

a=a*1.0/11520
print a
print str(sqrt(a))
#mseFile.write(str(mse[i])+" ")
mseFile.close()
jaccardFile.close()
minHashFile.close()      