import time


t1=time.time()
known_terms = []

with open('output.txt', 'r') as f:
    for line in f:
        toks = line.split()
        for t in toks:
            if t not in known_terms:
                known_terms.append(t)

print "Known terms = "+str(len(known_terms))

vector = []
with open('output.txt', 'r') as f:
    for line in f:
        toks = line.split()
        vec_line = [0]*len(known_terms)
        for t in toks:
            vec_line[known_terms.index(t)] = 1
        vector.append(vec_line)

print "vector done = "+str(len(vector))

k=128
import random
some_permutations = []
for x in xrange(k):
    some_permutations.append(random.sample(xrange(len(known_terms)), len(known_terms)))

def hash(permutation, vector):
    for x in permutation:
        if vector[x] != 0:
            return x

signature = []

for doc in vector:
    sign = []
    for perm in some_permutations:
        sign.append(hash(perm, doc))
    signature.append(sign)

print "signature done = "+str(len(signature))

def similarity(sign1, sign2):
    count = 0
    for x in xrange(len(sign1)):
        if sign1[x] == sign2[x]:
            count+=1
    return (count*1.0)/len(sign1)


similarity_matrix = []

out=open("similarity_matrix_time128.txt","w");

c=0
for x in xrange(len(signature)):
    simi = []
    c=0
    for y in xrange(len(signature)):
        #simi.append(similarity(signature[x], signature[y]))
        out.write(str(similarity(signature[x],signature[y]))+" ")
        c+=1
    #similarity_matrix.append(simi)
    out.write("\n")
    print "c="+str(c)
out.close()

t2=time.time()-t1
print "Time taken = "+str(t2)
