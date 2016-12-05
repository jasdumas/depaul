'''
Created on Mar 24, 2011
Ch 11 code
@author: Peter
'''
from numpy import *

def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
                
    C1.sort()
    return map(frozenset, C1)#use frozen set so we
                            #can use it as a key in a dict    

def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
 #              if not ssCnt.has_key(can): ssCnt[can]=1
                if can not in ssCnt: ssCnt[can]=1
                else: ssCnt[can] += 1
    numItems = len(D)
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minSupport:
            retList.insert(0,key)
        supportData[key] = support
    return retList, supportData

def aprioriGen(Lk, k): #creates Ck
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i+1, lenLk): 
            L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]
            L1.sort(); L2.sort()
            if L1==L2: #if first k-2 elements are equal
                retList.append(Lk[i] | Lk[j]) #set union
    return retList

def apriori(dataSet, minSupport = 0.5):
    C1 = createC1(dataSet)
    D = map(set, dataSet)
    L1, supportData = scanD(D, C1, minSupport)
    L = [L1]
    k = 2
    while (len(L[k-2]) > 0):
        Ck = aprioriGen(L[k-2], k)
        Lk, supK = scanD(D, Ck, minSupport)#scan DB to get Lk
        supportData.update(supK)
        L.append(Lk)
        k += 1
    return L, supportData

def generateRules(L, supportData, metric='confidence', minMetric=0.7):  #supportData is a dict coming from scanD
    bigRuleList = []
    for i in range(1, len(L)):#only get the sets with two or more items
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):
                rulesFromConseq(freqSet, H1, supportData, bigRuleList, metric, minMetric)
            else:
                calcMetric(freqSet, H1, supportData, bigRuleList, metric, minMetric)
    return bigRuleList         

def calcMetric(freqSet, H, supportData, brl, metric='confidence', minMetric=0.7):
    prunedH = [] #create new list to return
    for conseq in H:
        conf = supportData[freqSet]/supportData[freqSet-conseq] #calc confidence
        lift = conf/supportData[conseq] #calc lift
        if (metric == 'confidence'):
            if (conf >= minMetric): 
                print (freqSet-conseq,'-->',conseq,'conf:',conf,' lift:',lift)
                brl.append((freqSet-conseq, conseq, conf, lift))
                prunedH.append(conseq)
        elif (metric == 'lift'):
            if (lift >= minMetric): 
                print (freqSet-conseq,'-->',conseq,'conf:',conf,' lift:',lift)
                brl.append((freqSet-conseq, conseq, conf, lift))
                prunedH.append(conseq)
    return prunedH

def rulesFromConseq(freqSet, H, supportData, brl, metric='confidence', minMetric=0.7):
    m = len(H[0])
    if (len(freqSet) > (m + 1)): #try further merging
        Hmp1 = aprioriGen(H, m+1)#create Hm+1 new candidates
        Hmp1 = calcMetric(freqSet, Hmp1, supportData, brl, metric, minMetric)
        if (len(Hmp1) > 1):    #need at least two sets to merge
            rulesFromConseq(freqSet, Hmp1, supportData, brl, metric, minMetric)
            
def pntRules(ruleList, itemMeaning):
    for ruleTup in ruleList:
        for item in ruleTup[0]:
            print (itemMeaning[item])
        print ("           -------->")
        for item in ruleTup[1]:
            print (itemMeaning[item])
        print ("[confidence: %f, lift: %f]" % (ruleTup[2], ruleTup[3]))
        print()       #print a blank line
        
