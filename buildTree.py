# Chun Lin lin819@usc.edu
# Haoyu Jiang haoyujia@usc.edu

from math import log
import csv


def calcEntropy(dataset):
    lenSet = len(dataset)
    resultCount = {}
    sumResult = 0.0
    for line in dataset:
        if line[-1] not in resultCount.keys():  # result(y/n) and counts saved in resultCount
            resultCount[line[-1]] = 0
        resultCount[line[-1]] += 1
    for key in resultCount.keys():
        sumResult += float(resultCount[key])/lenSet * log(lenSet/float(resultCount[key]),2)
    return sumResult

def divideDs(dataset, attr):
    resultSets = {}
    for line in dataset:
        if line[attr] not in resultSets.keys():  # create a dict with key(types in attr) and value(subset)
            resultSets[line[attr]] = []
        resultSets[line[attr]].append(line)
    return resultSets

def majorityResult(dataset):
    resultCount = {}
    for line in dataset:
        if line[-1] not in resultCount.keys():
            resultCount[line[-1]] = 0
        resultCount[line[-1]] += 1
    return max(resultCount, key=lambda i: resultCount[i])

def constructTree(dataset, attrDict, lastEntropy):
    # Terminate condition: unanimous or run out of attributes
    if calcEntropy(dataset) == 0:
        return dataset[0][-1]
    if not attrDict:
        return majorityResult(dataset)

    # Compute the best attribute w/ info gain
    bestInfoGain = 0.0
    bestattr = None
    for attr in attrDict.keys():
        sumEntropy = 0.0
        resultSets = divideDs(dataset, attrDict[attr])
        for key in resultSets.keys():
            sumEntropy += calcEntropy(resultSets[key]) * (float(len(resultSets[key]))/len(dataset))
        infoGain = lastEntropy - sumEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestattr = attr
        elif infoGain == bestInfoGain:  # break tie, lower attr higher priority
            if bestattr == None or attrDict[attr] < attrDict[bestattr]:
                bestattr = attr

    if bestattr != None:
        bestEntropy = lastEntropy - bestInfoGain
        resultSets = divideDs(dataset, attrDict[bestattr])
        resDict = {bestattr: {}}
        newDict = dict(attrDict)  # create a replica, remove current attr then pass to next
        del (newDict[bestattr])
        for key in resultSets.keys():
            resDict[bestattr][key] = constructTree(resultSets[key], newDict, bestEntropy)
    else:
        return majorityResult(dataset)

    return resDict

def outputTree(treeDict, attrResultDict, level, levelDict):
    # Terminate condition: input treedict is not a dict
    if isinstance(treeDict, dict):
        levelDict[level].append(treeDict.keys()[0])
    else:
        levelDict[level].append(treeDict)
        return

    currentAttr = treeDict.keys()[0]  # Occupied
    nextlevel = level + 1
    if not levelDict.has_key(nextlevel):
        levelDict[nextlevel] = []
    for result in attrResultDict[currentAttr]:
        if treeDict[currentAttr].has_key(result):
            outputTree(treeDict[currentAttr][result], attrResultDict, nextlevel, levelDict)
        else:
            levelDict[nextlevel].append('Tie')

def makePrediction(prediction, resultDict):
    if not isinstance(resultDict, dict):
        print resultDict
    else:
        currentAttr = resultDict.keys()[0]
        attrRes = prediction[currentAttr]
        makePrediction(prediction, resultDict[currentAttr][attrRes])

f = open("testdata.txt", 'r')
attrNames = f.readline().strip().split(',')
del(attrNames[-1])  # remove the final result's name
attrDict = dict(zip(attrNames, range(len(attrNames)))) # dict to store {attribute: col_index}
reader = csv.reader(f)
originalDataset = list(reader)
f.close()
firstEntropy = calcEntropy(originalDataset)
treeResult = constructTree(originalDataset, attrDict, firstEntropy)
# print treeResult

attrResult = {'Size': ['Large','Medium','Small'],
              'Occupied': ['High', 'Moderate', 'Low'],
              'Price': ['Expensive', 'Normal', 'Cheap'],
              'Music': ['Loud', 'Quiet'],
              'Location': ['Talpiot', 'City-Center', 'Mahane-Yehuda', 'Ein-Karem', 'German-Colony'],
              'VIP': ['Yes', 'No'],
              'FavoriteBeer': ['Yes', 'No']}
leveldict = {0: []}
outputTree(treeResult, attrResult, 0, leveldict)
for key in leveldict.keys():
    print ', '.join(leveldict[key])

prediction = {'Size': 'Large',
              'Occupied': 'Moderate',
              'Price': 'Cheap',
              'Music': 'Loud',
              'Location': 'City-Center',
              'VIP': 'No',
              'FavoriteBeer': 'No'}

makePrediction(prediction, treeResult)
