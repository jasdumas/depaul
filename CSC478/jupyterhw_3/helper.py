from random import randint
import numpy as np
from numpy import *
from numpy import genfromtxt
from numpy import array

generated = []

def contains(rc):
    if len(generated) == 0:
        return False

    for n in range(len(generated)):
        if rc == generated[n]:
            return True
    return False

def shuffleMatrix(inMat):
    numRows = inMat.shape[0]
    numCols = inMat.shape[1]
    numElements = numRows * numCols
    f = np.mat(np.empty(shape=(numRows, numCols)))
    #print "Before shuffle: "
    #print inMat
    while(len(generated) != numElements):
        r=randint(0, numRows-1)
        c=randint(0, numCols-1)
        if contains((r,c)) == False:
            generated.append((r,c))
        else:
            continue
    k=0
    for i in range(numRows):
        for j in range(numCols):
            f[i,j] = inMat[generated[k]]
            k = k + 1
    return f

def pruneMat(data):
    prunedData=[]
    pindex = 0

    for i in range(data.shape[0]):
        row = data[i,:]
        rowList = row.tolist()
        indices = [k for k, x in enumerate(rowList) if x!= 0]
        freq = len(indices)
        if(freq >= 10):
            pindex = pindex + 1
            prunedData.append(rowList)
    pruned=np.vstack(prunedData)
    prunedMat = np.mat(pruned)
    print ("pruned shape is: ", pruned.shape)
    print ("prunedMat shape is: ", prunedMat.shape)
    return prunedMat

def distCosine(vecA, vecB):
    #D_norm = array([linalg.norm(data[i]) for i in range(len(data))])
    #x_norm = linalg.norm(inX)
    #cosines = dot(data,inX)/(D_norm * x_norm)
    #distances = 1 - cosines

    norm_A = linalg.norm(vecA)
    norm_B = linalg.norm(vecB)
    cosine = dot(vecA, vecB) / norm_A * norm_B
    distance = 1 - cosine
    return distance

def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2))) #la.norm(vecA-vecB)
