from numpy import *
from numpy import linalg as la
import numpy as np

def ecludSim(inA,inB):
    return 1.0 / (1.0 + la.norm(inA - inB))

def pearsSim(inA,inB):
    if len(inA) < 3 : return 1.0
    return 0.5 + 0.5 * corrcoef(inA, inB, rowvar = 0)[0][1]

def cosSim(inA,inB):
    num = float(inA.T * inB)
    denom = la.norm(inA)*la.norm(inB)
    return 0.5 + 0.5 * (num / denom)

def standEst(dataMat, user, simMeas, item):
    n = shape(dataMat)[1]
    simTotal = 0.0; ratSimTotal = 0.0
    for j in range(n):
        userRating = dataMat[user,j]
        if userRating == 0: continue
        overLap = nonzero(logical_and(dataMat[:,item]>0, \
                                      dataMat[:,j]>0))[0]
        if len(overLap) == 0: similarity = 0
        else: similarity = simMeas(dataMat[overLap,item], \
                                   dataMat[overLap,j])
        #print 'the %d and %d similarity is: %f' % (item, j, similarity)
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0: return 0
    else: return ratSimTotal/simTotal
    
def svdEst(dataMat, user, simMeas, item):
    n = shape(dataMat)[1]
    simTotal = 0.0; ratSimTotal = 0.0
    data=mat(dataMat)
    U,Sigma,VT = la.svd(data)
    Sig4 = mat(eye(4)*Sigma[:4]) #arrange Sig4 into a diagonal matrix
    xformedItems = data.T * U[:,:4] * Sig4.I  #create transformed items
    for j in range(n):
        userRating = data[user,j]
        if userRating == 0 or j==item: continue
        similarity = simMeas(xformedItems[item,:].T,\
                             xformedItems[j,:].T)
        #print 'the %d and %d similarity is: %f' % (item, j, similarity)
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0: return 0
    else: return ratSimTotal/simTotal

# This function is not needed for Assignment 4, but may be useful for experimentation
def recommend(dataMat, user, N=3, simMeas=cosSim, estMethod=standEst):
    unratedItems = nonzero(dataMat[user,:].A==0)[1] #find unrated items 
    if len(unratedItems) == 0: return 'you rated everything'
    itemScores = []
    for item in unratedItems:
        estimatedScore = estMethod(dataMat, user, simMeas, item)
        itemScores.append((item, estimatedScore))
    return sorted(itemScores, key=lambda jj: jj[1], reverse=True)[:N]

# This function performs cross-validation on a single user based on the test_ratio
# For example, with test_ratio = 0.2, 5-fold x-validation is performed where in each fold, 
# 20 percent of rated items are withheld and the rest are used to estimate the withheld ratings

def cross_validate_user(dataMat, user, test_ratio, estMethod=standEst, simMeas=pearsSim):
    number_of_items = np.shape(dataMat)[1]
    rated_items_by_user = np.array([i for i in range(number_of_items) if dataMat[user,i]>0])
    test_size = test_ratio * len(rated_items_by_user)
    test_indices = np.random.randint(0, len(rated_items_by_user), test_size)
    withheld_items = rated_items_by_user[test_indices]
    original_user_profile = np.copy(dataMat[user])
    dataMat[user, withheld_items] = 0 # So that the withheld test items is not used in the rating estimation below
    error_u = 0.0
    count_u = len(withheld_items)

    # Compute absolute error for user u over all test items
    for item in withheld_items:
        # Estimate rating on the withheld item
        estimatedScore = estMethod(dataMat, user, simMeas, item)
        error_u = error_u + abs(estimatedScore - original_user_profile[item])	
    
    # Now restore ratings of the withheld items to the user profile
    for item in withheld_items:
        dataMat[user, item] = original_user_profile[item]
        
    # Return sum of absolute errors and the count of test cases for this user
    # Note that these will have to be accumulated for each user to compute MAE
    return error_u, count_u
    
def test(dataMat, test_ratio, estMethod):
    # Write this function to iterate over all users and for each perform cross-validation on items by calling
    # the above cross-validation function on each user.
    # MAE will be the ratio of total error across all test cases to the total number of test cases, for all users
    
    #row = dataMat[0,]
    #print "A row is: ", row
    total_error=0.0
    total_count=0
    for user in range(dataMat.shape[0]):
        error, count = cross_validate_user(dataMat, user, .2, standEst)
        total_error = total_error + error
        total_count = total_count + count
    MAE = total_error/total_count
    print ('Mean Absoloute Error for ',estMethod,' : ', MAE)
    return MAE

def print_most_similar_jokes(dataMat, jokes, queryJoke, k, metric=pearsSim):
    # Write this function to find the k most similar jokes (based on user ratings) to a queryJoke
    # The queryJoke is a joke id as given in the 'jokes.csv' file (an corresponding to the a column in dataMat)
    # You must compare ratings for the queryJoke (the column in dataMat corresponding to the joke), to all
    # other joke rating vectors and return the top k. Note that this is the same as performing KNN on the 
    # columns of dataMat. The function must retrieve the text of the joke from 'jokes.csv' file and print both
    # the queryJoke text as well as the text of the returned jokes.
    queryJokeVector = dataMat[:,queryJoke]
    print ("Selcted joke: ")
    print()
    print (jokes[queryJoke])
    print()
    dataMatArray = np.array(dataMat)
    knn, indicies = kNearestNeighbors(queryJokeVector, dataMat, k, metric)	
    print ("The top %d recommended jokes are: "%(k))
    for ind in indicies:
        jok = jokes[ind]
        print()
        print (jok)
    #print "Done"

def kNearestNeighbors(inX, dataSet, k, measure):
    distances = []
    for i in range(dataSet.shape[1]):
        vector = dataSet[:,i]
        distance = measure(inX, vector)
        distances.append(distance)
    #print "Before, distances is: ", distances
    distancesArray = np.array(distances)
    #print "After, distances is: ", distancesArray
    sortedDistIndicies = distancesArray.argsort()
    kNeighbors = zeros((k,dataSet.shape[1]))
    topIndicies = []
    classCount={}
    for i in range(k):
        #voteIlabel = labels[sortedDistIndicies[i]]
        kNeighbors[i,:] = dataSet[sortedDistIndicies[i],:]
        topIndicies.append(sortedDistIndicies[i])
        #print "sortedDistIndices: is", sortedDistIndicies
        #print "kNeighbors is: ", kNeighbors
        #classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    #sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1), reverse=True)
    return kNeighbors, topIndicies  #, sortedClassCount[0][0]

def load_jokes(file):
    jokes = genfromtxt(file, delimiter=',', dtype=str)
    jokes = np.array(jokes[:,1])
    return jokes

def get_joke_text(jokes, id):
    return jokes[id]

# dataMat = genfromtxt('modified_jester_data.csv',delimiter=',')

# test(dataMat, 0.2, svdEst)
# test(dataMat, 0.2, standEst)

# jokes = load_jokes('jokes.csv')
# print_most_similar_jokes(dataMat, jokes, 3, 5, pearsSim)

''' See example output below:

Selected joke: 

Q. What's the difference between a man and a toilet? A. A toilet doesn't follow you around after you use it.

Top 5 Recommended jokes are :

Q: What's the difference between a Lawyer and a Plumber? A: A Plumber works to unclog the system. 
_______________
What do you call an American in the finals of the world cup? "Hey Beer Man!" 
_______________
Q. What's 200 feet long and has 4 teeth? <P>A. The front row at a Willie Nelson Concert. 
_______________
A country guy goes into a city bar that has a dress code and the maitred' demands he wear a tie. Discouraged the guy goes to his car to sulk when inspiration strikes: He's got jumper cables in the trunk! So he wrapsthem around his neck sort of like a string tie (a bulky string tie to be sure) and returns to the bar. The maitre d' is reluctant but says to the guy "Okay you're a pretty resourceful fellow you can come in... but just don't start anything"!   
_______________
What do you get when you run over a parakeet with a lawnmower? <P>Shredded tweet. 
_______________

'''
