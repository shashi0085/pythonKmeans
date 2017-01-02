
import nose.tools as nt  # contains testing tools like ok_, eq_, etc.
import kmeans.kmeansFile

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def testing4():
    initK = 2
    (centroids,c, k, iters, points) = kmeans.kmeansFile.kmeansAlgo(initK, 1000, 0.001, "kmeans/inputfile")
    assert iters <= 1000
    assert len(centroids) <= initK
    assert k <= initK

def testDistaceFromCentroids():
    initK = 10
    (centroids, c, k, iters, points) = kmeans.kmeansFile.kmeansAlgo(2, 1000, 0.00001, "kmeans/inputfile", False, 0, 30, 0, 30, 5) #kmeans.kmeansFile.kmeansAlgo(initK, 1000, 0.00001, "kmeans/inputfile")
    for i in range(len(points)):
        cluster = c[i]
        centroid = centroids[cluster]
        internalDist = kmeans.kmeansFile.dist(centroid, points[i])
        for k in range(len(centroids)):
            if k != cluster:
                #distance of point to it's own centroid should be less than all other centroids
                assert (kmeans.kmeansFile.dist(points[i], centroids[k]) > internalDist)


def testInternalDistance():
    initK = 5
    (centroids, c, k, iters, points) = kmeans.kmeansFile.kmeansAlgo(initK, 1000, 0.001, "kmeans/inputfile")
    for i in range(len(points)):
        cluster = c[i]
        centroid = centroids[cluster]
        internalDist = kmeans.kmeansFile.dist(centroid, points[i])
        #in this case distance between any point to it's centroid should be less than 1.5
        assert internalDist < 1.5







