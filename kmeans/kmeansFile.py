import numpy as np
from random import randint
from random import uniform
from decimal import *

def initialize(k, dataPoints, length):
    xPoints = dataPoints[:, 0]
    yPoints = dataPoints[:, 1]
    minX = min(xPoints)
    maxX = max(xPoints)
    minY = min(yPoints)
    maxY = max(yPoints)
    centroids = [[0 for x in range(2)] for y in range(k)]
    for i in range(k):
        centroids[i][0] = uniform(minX, maxX)
        centroids[i][1] = uniform(minY, maxY)
    c = [-1 for x in range(length)]
    return (centroids, c)


def kmeansAlgo(k, maxIter, maxThreshold, filename= "inputfile", takeFromfile = True, minX = 0, maxX = 0, minY = 0, maxY = 0, count = 0):

    dataPoints = np.array([[]])
    if(takeFromfile):
        dataPoints = readFromFile(filename)
    else:
        dataPoints = randomPointGenerator(minX, maxX, minY, maxY, count)

    print(dataPoints)

    dataLength = len(dataPoints)
    (centroids, c) = initialize(k, dataPoints, dataLength)
    #centroids = [[24.3295886026,64.9411220681], [49.4283053303,51.0731237426], [63.9379560324,65.0055440159]]
    print(centroids)

#initial clustering
    for ex in range(dataLength):
        minDist = dist(dataPoints[ex], centroids[0])
        cluster = 0
        for c_iter in range(1, k):
            cdist = dist(dataPoints[ex], centroids[c_iter])
            if(cdist < minDist):
                minDist = cdist
                cluster = c_iter
            c[ex] = cluster

    threshold = maxThreshold+1
    iters = 0;
    while (threshold > maxThreshold and maxIter > iters):
        #centroid step
        tempC = [[0 for x in range(2)] for y in range(k)]
        testC = [[0 for x in range(2)] for y in range(k)]
        tempCount = [0 for x in range(k)]
        for ex in range(dataLength):
            whichCluster = c[ex]
            assert(whichCluster < len(tempC))
            tempC[whichCluster][0] += dataPoints[ex][0]
            tempC[whichCluster][1] += dataPoints[ex][1]
            tempCount[whichCluster] += 1
            c_iter = 0
        for cluster in range(k):
            if(tempCount[cluster]  > 0):
                #only keep the clusters that are non empty.
                testC[cluster] = centroids[cluster]
                tempC[cluster][0] = tempC[cluster][0] / tempCount[cluster]
                tempC[cluster][1] = tempC[cluster][1] / tempCount[cluster]
                #c_iter += 1
            #else:
             #   k -= 1 #if a cluster contains nothing, drop it.

        threshold = distInCentroids(testC, tempC)

        centroids = tempC
        print("new centroids: ", centroids)

        #clustering step
        for ex in range(dataLength):
            minDist = dist(dataPoints[ex], centroids[0])
            cluster = 0
            for c_iter in range(1, k):
                cdist = dist(dataPoints[ex], centroids[c_iter])
                if(cdist < minDist):
                    minDist = cdist
                    cluster = c_iter
            c[ex] = cluster

        iters += 1

    print(centroids[:k])
    print(c)
    print("iters: ", iters)
    return (centroids[:k], c, k, iters, dataPoints)

def dist(point1, point2):
    return ((point2[0]-point1[0])**2 + (point2[1] - point1[1])**2)**0.5



def readFromFile(filename):
    lines = [line.rstrip('\n') for line in open(filename)]
    length = len(lines)
    mypoints = [[0 for x in range(2)] for y in range(length)]
    index = 0
    for line in lines:
        points = line.split(",")
        mypoints[index][0] = float(points[0])
        mypoints[index][1] = float(points[1])
        index += 1

    dataPoints = np.array(mypoints)
    return dataPoints


def randomPointGenerator(minX, maxX, minY, maxY, count):
    points = [[uniform(minX, maxX), uniform(minY, maxY)] for x in range(count)]
    print("points ", points)
    dataPoints =  np.array(points)
    print("i came in here")
    print(dataPoints)
    return dataPoints


def distInCentroids(oldC, newC):
    max = dist(oldC[0], newC[0])
    assert len(oldC) == len(newC)
    length = len(oldC)
    for i in range(1, length):
        newDist = dist(oldC[i], newC[i])
        if newDist > max:
            max = newDist
    return max

if __name__ == "__main__":
    kmeansAlgo(2, 1000, 0.00001, "inputfile")
    #kmeansAlgo(5, 1000, 0.00001, "random", False, 0, 300, 0, 300, 200)

def testing():
    return 1


