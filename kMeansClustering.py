

#import matplotlib.pyplot as plt
import math
import random
import sys


# READ FILE
def readCandidatesFile(fileName):
    '''
    Reads and processes the file, returning 4 lists: 
    <List of candidates names, list of lists with the 
    features of the candidates, list of examplars names,
    list of lists with the exemplars features>.

    Requires: fileName is str.

    Ensures: <List of candidates names, 
    List of candidates features,
    List of exemplars names,
    List of exemplars features>
    '''
    nameList = []
    featureList = [] #List of list of strs
    endOfCandidates = False
    exemplarsName = []
    exemplars = []
    # try:
    with open(fileName, encoding='utf-8') as myFile:
        for line in myFile:
            line = line.strip('\n')

            if not line.startswith('#'):
                if not endOfCandidates:
                    feature = line.split('; ')
                    name = feature.pop(0)
                    nameList.append(name)
                    featureList.append(feature)                   
                else:
                    feature = line.split('; ')
                    name = feature.pop(0)
                    exemplarsName.append(name)
                    exemplars.append(feature)

            if line == "#Exemplars:":
                endOfCandidates = True

    return nameList, featureList, exemplarsName, exemplars

    # except FileNotFoundError:
    #     print("FileNotFoundError: No such file or" + \
    #         " directory: {}".format(fileName))
    #     sys.exit(1)

def readTitlesFile(fileName):
    '''
    Reads and processes the titles file.
    
    Requires: fileName is str.

    Ensures: <List of score (int), List of titles 
    (str, len=2)>
    '''
    scoreList = []
    titlesList = []
    #dic = {}
    with open(fileName, encoding='utf-8') as myFile:
        for line in myFile:
            if not line.startswith('#'):
                line = line.strip('\n')
                titles = line.split('; ')
                score = titles.pop(0)
                scoreList.append(int(score))
                titlesList.append(titles)
                ## com dic
                #dic[titles[0]] = score
                #dic[titles[1]] = score
                ##
    #return dic
    return scoreList, titlesList

# END OF READ FILE

# TRANSLATE CONTENT TO FEATURE VECTOR

def translateTitleToScore(scores, titles, title, k):
    '''
    Convertes a title to it's respective 
    score and returns it.

    Requires: title is str
    '''
    i = 0

    for j in range(len(titles)):
        if titles[j][k] == title:
            return scores[j]

def translateToFeatureVector(scores, titles, featureList):
    '''
    Translates all the titles from a candidate to a 
    feature vector of int.

    Requires: content is list of titles
    '''
    list = []
    i = 0
    for title in featureList:
        # featureList = [duque, duquesa, rei, rainha, ... , ...]
        if (i % 2) == 0: # Its masculine
            k = 0
        else: # Its feminine
            k = 1
        
        score = translateTitleToScore(scores, \
                    titles, title, k)
        list.append(score)

        i += 1
    return list


# END OF TRANSLATE CONTENT TO FEATURE VECTOR

# WRITE FILE
def writeFile(fileName, content):
    '''
    Procudes the output file

    Requires: fileName is str, file name for the
    new file; content is str, content to write the
    file with.
    '''
    with open(fileName, 'w') as f: # talvez por aqui tbm encoding="utf-8"
        f.write(content)

############## 24.2 Distance Metrics



# Minkowski distance

def minkowskiDist(v1, v2, p):
    """
    Minkowski distance
    
    Requires:
    v1 and v2 are equal-dimension lists of numbers,
    representing feature vectors;
    p represents Minkowski order
    Ensures:
    Minkowski distance of order p between v1 and v2
    """
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1.0/p)


# Testing

##cascavel = [1,1,1,1,0]
##jiboia = [0,1,0,1,0]
##print("Euclidean distance:", minkowskiDist(cascavel, jiboia, 2))
##print("Manhattan distance:", minkowskiDist(cascavel, jiboia, 1), "\n")



# First case study with animals 

class Animal(object):
    """
    Animal
    """

    
    def __init__(self, name, features):
        """
        Constructor
    
        Requires:
        name a string representing the name of the animal;
        features a list of numbers representing its feature vector
        Ensures:
        object of type Animal created
        """
        self._name = name
        self._features = features


    def getName(self):
        """
        Name of the animal

        Ensures:
        name of animal
        """
        return self._name


    def getFeatures(self):
        """
        Feature vector of the animal

        Ensures:
        list representing the feature vector of the animal
        """
        return self._features


    def distance(self, other):
        """
        Euclidean distance with respect to a given animal

        Requires:
        other is an animal
        Ensures:
        the Euclidean distance between feature vectors of self and other
        """
        return minkowskiDist(self.getFeatures(), other.getFeatures(), 2)


##    def __str__(self): #to be implemented
##            pass
##        
##    def __eq__(self): #to be implemented
##            pass
##
##    def __lt__(self): #to be implemented
##            pass



def compareAnimals(animals, precision):
    """
    Compares animals

    Requires:
    animals a list of animals;
    precision int >= 0 representing comparison precision.
    Ensures:
    Save to file table with Euclidean distance between
    the feature vectors of each animal in animals
    """
    #Get labels from columns and rows
    columnLabels = []
    for a in animals:
        columnLabels.append(a.getName())
    rowLabels = columnLabels[:]
    tableVals = []
    #Get distance between pairs of animals
    #For each row
    for a1 in animals:
        row = []
        #For each column
        for a2 in animals:
            distance = a1.distance(a2)
            row.append(str(round(distance, precision)))
        tableVals.append(row)
    #Produce table
    # table = plt.table(rowLabels = rowLabels,
    #                     colLabels = columnLabels,
    #                     cellText = tableVals,
    #                     cellLoc = "center",
    #                     loc = "center",
    #                     colWidths = [0.2]*len(animals))
    # plt.axis("off")
    # table.scale(1, 2.5)
    # plt.savefig("distances")
    # plt.show()


##cascavel = Animal('cascavel', [1,1,1,1,0,1])
##jiboia = Animal('jiboia', [0,1,0,1,0,1])
##crocodilo = Animal('crocodilo', [1,1,0,1,4,1])
##ra = Animal('ra do dardo', [1,0,1,0,4,1])
##salmao = Animal('salmao', [1,1,0,1,0,0])
##animals = [cascavel, jiboia, crocodilo, ra, salmao]
##compareAnimals(animals, 3)



############## 25.1 Types Example and Cluster



class Example(object):
    """
    Example for clustering
    """

    def __init__(self, name, features, label = None):
        """
        Constructor

        Requires:
        features is list of numbers representing the feature vector;
        label is string with the label of the example
        Ensures:
        object of type Example created
        """
        self._name = name
        self._features = features
        self._label = label


    def dimensionality(self):
        """
        Dimensionality of the feature vector

        Ensures:
        dimensionality of the feature vector
        """
        return len(self._features)


    def setName(self, name):
        """
        Name setting

        Ensures:
        self._name = name
        """
        self._name = name

        
    def setFeatures(self, features):
        """
        Features setting

        Ensures:
        self._features = features
        """
        self._features = features
        

    def setLabel(self, label):
        """
        Label setting

        Ensures:
        self._label = label
        """
        self._label = label

    
    def getFeatures(self):
        """
        Features

        Ensures:
        feature vector
        """
        return self._features[:]


    def getLabel(self):
        """
        Object label

        Ensures:
        object label
        """
        return self._label


    def getName(self):
        """
        Object Name

        Ensures:
        object name
        """
        return self._name


    def distance(self, other):
        """
        Euclidean distance wrt a given example

        Requires:
        other is an example
        Ensures:
        the Euclidean distance between feature vectors
        of self and other
        """
        return minkowskiDist(self._features, other.getFeatures(), 2)


    def __str__(self):
        """
        String representation

        Ensures:
        string representation in the form "name:features:label"
        """
        return self._name + ':' + str(self._features) + ':' + str(self._label)

    def __eq__(self, otherObj): # Do I need really this? The original Example and kmeans does need this...
        '''
        Verifies if self is equal to another Example

        Requires: otherObj is Example object
        
        Ensures: bool 
        True is both Example objects have equal: name and feature.
        False otherwise.
        '''
        
        if self.getName() != otherObj.getName():
            return False

        if len(self.getFeatures()) != len(otherObj.getFeatures()):
            return False
        
        # Not tested
        i = 0
        for feature in self.getFeatures():
            featuresOtherObj = otherObj.getFeatures()
            if feature != featuresOtherObj[i]:
                return False
            i += 1

        return True


##    def __eq__(self): #to be implemented
##            pass
##
##
##    def __lt__(self): #to be implemented
##            pass
        


class Cluster(object):
    """
    Cluster of examples
    """
    
    def __init__(self, examples):
        """
        Constructor

        Requires:
        examples is a list of objects of a type that has
        a method returning the list of features of an object and
        a method returning the distance among them;
        Ensures:
        object of type Cluster is created
        """
        self._examples = examples
        self._centroid = self.computeCentroid()


    def update(self, examples):
        """
        Update the cluster with a given collection of examples

        Requires:
        examples a list of objects of the type of members in self._examples
        Ensures:
        examples = getExamples();
        returns how much the centroid has changed
        """
        oldCentroid = self._centroid
        self._examples = examples
        if len(examples) > 0:
            self._centroid = self.computeCentroid()
            return oldCentroid.distance(self._centroid)
        else:
            return 0.0


    def computeCentroid(self):
        """
        Compute centroid of the cluster

        Ensures:
        centroid of the cluster
        """
        dim = self._examples[0].dimensionality()
        totVals = [0]*dim
        for e in self._examples:
            for i in range(dim):
                totVals[i] = totVals[i]+e.getFeatures()[i]
        totValsAveraged = []
        for i in range(dim):
            totValsAveraged.append(totVals[i]/float(len(self._examples)))
        centroid = Example('centroid', totValsAveraged)
        return centroid
    

    def getExamples(self):
        """
        Examples in the cluster

        Ensures:
        list with examples in the cluster
        """
        return self._examples


    def getCentroid(self):
        """
        Centroid of the cluster

        Ensures:
        centroid of the cluster
        """
        return self._centroid

            
    def size(self):
        """
        Size of the cluster

        Ensures:
        number of examples in cluster
        """
        return len(self._examples)
    

    def variability(self):
        """
        Variability

        Ensures:
        variance of the cluster
        """
        totDist = 0.0
        for e in self._examples:
            totDist += (e.distance(self._centroid))**2
        return totDist
    

    def members(self):
        """
        Generator method
        """
        for e in self._examples:
            yield e
            

    def __str__(self):
        """
        String representation

        Ensures:
        string representation in the form
        "Cluster with centroid [...] contains:
         ex1 ex2 ... exN "
        """
        names = []
        for e in self._examples:
            names.append(e.getName())
        names.sort()
        result = 'Cluster with centroid '\
                 + str(self._centroid.getFeatures()) + ' contains:\n'
        for e in names:
            result = result + e + ', '
        return result[:-2] #remove trailing comma and space


##    def __eq__(self):  #to be implemented
##            pass
##
##
##    def __lt__(self):  #to be implemented
##            pass




##cascavel = Example('cascavel', [1,1,1,1,0,1])
##jiboia = Example('jiboia', [0,1,0,1,0,1])
##crocodilo = Example('crocodilo', [1,1,0,1,4,1])
##ra = Example('ra do dardo', [1,0,1,0,4,1])
##salmao = Example('salmao', [1,1,0,1,0,0])
##
##examples = [cascavel, jiboia, crocodilo, ra, salmao]
##animals = Cluster(examples)
##
##print(animals.getCentroid())
##print()
##
##print(animals.variability())
##print()
##
##print(animals)
##print()



############## 25.2 K-means Clustering



def kmeans(examples, initialCentroids, k, verbose):
    """
    K-means clustering
    
    Requires:
    examples a list of examples of a same type;
    k positive int, number of clusters;
    verbose Boolean, printing details on/off
    Ensures:
    list containing k clusters;
    if verbose is True, result of each iteration
    of k-means is printed
    """
    #Get k randomly chosen initial centroids, create cluster for each
    #initialCentroids = random.sample(examples, k)
    initialCentroids = initialCentroids
    
    clusters = []
    for e in initialCentroids:
        clusters.append(Cluster([e]))

    #Iterate until centroids do not change
    converged = False
    numIterations = 0
    while not converged:
        
        numIterations += 1

        #Create a list containing k distinct empty lists
        newClusters = []
        for i in range(k):
            newClusters.append([])

        #Associate each example with closest centroid
        for e in examples:
            #Find the centroid closest to e
            smallestDistance = e.distance(clusters[0].getCentroid())
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            #Add e to the list of examples for the appropriate cluster
            newClusters[index].append(e)

        #Avoid having empty clusters
        for c in newClusters:
            if len(c) == 0:
                raise ValueError("Empty Cluster")

        #Update each cluster; check if a centroid has changed
        converged = True
        for i in range(len(clusters)):
            if clusters[i].update(newClusters[i]) > 0.0:
                converged = False

        #Trace intermediate levels of clustering if verbose on
        if verbose:
            print('Iteration #' + str(numIterations))
            for c in clusters:
                print(c)
            print('') #add blank line
            
    return clusters

#Feature vector: egg-laying; scales; posionous; cold-blooded; #legs; reptile
##cascavel = Example('cascavel', [1,1,1,1,0,1])
##jiboia = Example('jiboia', [0,1,0,1,0,1])
##crocodilo = Example('crocodilo', [1,1,0,1,4,1])
##ra = Example('ra do dardo', [1,0,1,0,4,1])
##salmao = Example('salmao', [1,1,0,1,0,0])
##lagarto = Example('lagarto', [1,0,0,1,4,1])
##carapau = Example('carapau', [1,0,0,0,1,0])
##leopardo = Example('leopardo', [0,0,0,0,0,0])
##
##examples = [cascavel, jiboia, crocodilo, ra, salmao, lagarto, carapau, leopardo]
##
##kmeans(examples, 3, True)



def dissimilarity(clusters):
    """
    Dissimilarity among clusters

    Ensures:
    dissimilarity among clusters as the summation
    of each cluster variance
    """
    totDist = 0.0
    for c in clusters:
        totDist += c.variability()
    return totDist



def trykmeans(examples, numClusters, numTrials,
              verbose = False):
    """
    Best clustering outcome within a given number of trials
    of k-means clustering

    Requires:
    examples a list of examples of a same type;
    numClusters positive int, number of clusters;
    numTrials positive int, number of trials with k-means clustering
    Ensures:
    The clusters obtained with the lowest dissimilarity among them
    after running k-means clustering numTrials times over examples
    """
    best = kmeans(examples, numClusters, verbose)
    minDissimilarity = dissimilarity(best)
    print("\ncluster1: " + str(minDissimilarity))
    
    for trial in range(1, numTrials):
        clusters = kmeans(examples, numClusters, verbose)
        currDissimilarity = dissimilarity(clusters)
        print("cluster" + str((trial+1)) + " " + str(currDissimilarity))
        if currDissimilarity < minDissimilarity:
            best = clusters
            minDissimilarity = currDissimilarity
            
    return best




        
############## 25.3 A Contrived Example



def genDistribution(xMean, xSD, yMean, ySD, n, namePrefix):
    """
    Randomly generates 2D points

    Requires:
    xMean number representing the mean in x-axis
    xSD number representing standard deviation in x-axis
    yMean number representing the mean in x-axis
    ySD number representing standard deviation in x-axis
    n positive int, number of points to be generated
    namePrefix string, prefix for naming
    Ensures:
    list of 2D points randomly generated under the parameters
    in the pre-conditions
    """
    samples = []
    for s in range(n):
        x = random.gauss(xMean, xSD)
        y = random.gauss(yMean, ySD)
        samples.append(Example(namePrefix+str(s), [x, y]))
    return samples



def plotSamples(samples, marker):
    """
    Plot of a given list of 2D points

    Requires:
    samples list with 2D points;
    marker matplotlib indicator of shape and color
    Ensures:
    2D plot with points shaped as marker
    """
    xVals, yVals = [], []
    for s in samples:
        x = s.getFeatures()[0]
        y = s.getFeatures()[1]
    #     plt.annotate(s.getName(), xy = (x, y),
    #                    xytext = (x+0.13, y-0.07),
    #                    fontsize = 'x-large')
    #     xVals.append(x)
    #     yVals.append(y)
    # plt.plot(xVals, yVals, marker)



def contrivedTest(numTrials, k, verbose):
    """
    Testing k-means with a test case

    Requires;
    numTrials positive int, number of trials for k-means clustering;
    k positive int, number of clusters to be formed;
    verbose Boolean, printing details on/off
    Ensures:
    test runned
    """
    #random.seed(0)
    random.seed()
    xMean = 3
    xSD = 1
    yMean = 5
    ySD = 1
    n = 10
    d1Samples = genDistribution(xMean, xSD, yMean, ySD, n, 'A')
    plotSamples(d1Samples, 'k^')
    d2Samples = genDistribution(xMean+3, xSD, yMean+1, ySD, n, 'B')
    plotSamples(d2Samples, 'ko')
    # plt.show()
    clusters = trykmeans(d1Samples + d2Samples, k,
                         numTrials, verbose)
    print('Final result')
    for c in clusters:
        print('', c)


#contrivedTest(3, 4, True)






                
    





