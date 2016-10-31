import numpy as np
from numpy import array
from numpy import *
import operator

def createDataSet(filename, size):
    fr = open(filename)
    numOfLines = len(fr.readlines())
    #print "Number of lines: ", numOfLines
    #retMat = zeros((numOfLines, 800))
    retMat = zeros((size, numOfLines))
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        retMat[:,index]=listFromLine[0:]
        index = index + 1
    return retMat

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m,1))
    normDataSet = normDataSet/tile(ranges, (m,1))
    return normDataSet, ranges, minVals

def createLabelsVector(filename):
    labelsVector = ["0", "1"]
    fr = open(filename)
    numOfLines = len(fr.readlines())
    #print "Number of lines: ", numOfLines
    #retMat = zeros((numOfLines, 3))
    classLabelVector = []
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        classLabelVector.append(labelsVector.index(listFromLine[-1]))
        index = index + 1
    return classLabelVector

def classifyTest(dataMat, testMat, measure, k):
    #dataMat = createDataSet('newsgroups/trainMatrixModified.txt', 800)
    #testMat = createDataSet('newsgroups/testMatrixModified.txt', 200)
    labels = createLabelsVector('trainClasses.txt')
    testlabels = createLabelsVector('testClasses.txt')
    normDataMat, ranges, minVals = autoNorm(dataMat)
    normTestMat, testRanges, testMinVals = autoNorm(testMat)
    hits = 0.0
    for i in range(len(testMat)):
        classifierResult = classify(testMat[i,:], dataMat, labels, k, measure)
        if (classifierResult[1] == testlabels[i]):
            hits += 1.0
    successRate = hits/float(len(testMat))
    #print "The total success rate is: %1.2f"% ()) + "%"
    return successRate



def classify(inX, dataSet, labels, k, measure):
    distances = []
    if measure == 'CosineSimilarity':
        distances = getCosineDistances(inX, dataSet)
    else:
        distances = getEuclideanDistances(inX, dataSet)
    sortedDistIndicies = distances.argsort()
    kNeighbors = zeros((k,dataSet.shape[1]))
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        kNeighbors[i,:] = dataSet[sortedDistIndicies[i],:]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1), reverse=True)
    return kNeighbors, sortedClassCount[0][0]

def getCosineDistances(inX, data):
    #print "getCosineDistances"
    dataSetSize = data.shape[0]
    D_norm = array([linalg.norm(data[i]) for i in range(len(data))])
    x_norm = linalg.norm(inX)
    cosines = dot(data,inX)/(D_norm * x_norm)
    distances = 1 - cosines
    return distances

def getEuclideanDistances(inX, data):
    #print "getEuclideanDistances"
    dataSetSize = data.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - data
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    return distances

def numDocsContainingTerm(row):
    rowList = row.tolist()
    indicies = [i for i, x in enumerate(rowList) if x!= 0]
    return len(indicies)

def generateWeightedMatrix(orig):
    freqs = orig.shape[0]
    docs = orig.shape[1]
    weightMatrix = zeros((freqs, docs))
    tc = 0
    for f in range(0,freqs):
        nk=numDocsContainingTerm(orig[f,:])
        for d in range(0,docs):
            tfik=orig[f,d]
            x = docs/float(nk)
            idfk = math.log((x), 2)
            w = tfik*idfk
            weightMatrix[f,d] = w
    np.set_printoptions(precision=2, suppress=True,linewidth=120)
    return weightMatrix
