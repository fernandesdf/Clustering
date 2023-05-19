from kMeansClustering import kmeans, trykmeans, Example, \
    dissimilarity, readCandidatesFile, writeFile, \
    translateToFeatureVector, readTitlesFile, \
    getRealCentroid, processOutputString, writeFile
from CommandInputError import CommandInputError


#import matplotlib.pyplot as plt

# PASSOS
#1 fazer classe candidate
#2 ler ficheiros (candidates.txt e titles.txts)
#3 fazer metodo q me faca a traducao do dos candidates para vector
#   (input file)
#4 fazer metodo que faca a traducao de vector para output file
#   feactures (utilizando o titles.txt) 
#5 (1. if no main para separar se tem q passar examplars para o 
#    cluster ou nao;
#   2. alterar cluster
#    if examplars = None
#       pass
#    else
#       examplars, exampleList = findExamplars(clusters)
# ) #n entendo como eh suposto funcionar o findExamples

#...
#6 (1. Em cada cluster encontrar o centroid real;
#   2. Cluster ficar como centroid um centroid real, ex Paulo, 
#    em vez de 1 centroid artificial ideial.
# )


# ****** || ******





######### || ########
# (readCandidatesFile)
candidatesNames, candidatesTitles, exemplarsName, exemplarsTitles \
      = readCandidatesFile('candidates.txt')

print("candidatesNames")
print(candidatesNames)
print()
print("candidatesTitles")
print(candidatesTitles)
print()
print("exemplarsName")
print(exemplarsName)
print()
print("exemplars")
print(exemplarsTitles)
print()


scoresList, titlesList = readTitlesFile('titles.txt')

print("scoresList")
print(scoresList)
print("titlesList")
print(titlesList)

candfeatureVectors = []
for titles in candidatesTitles:
    featureVector = translateToFeatureVector(scoresList, \
                       titlesList, titles)
    candfeatureVectors.append(featureVector)

print()
print("candidates feature vector")
print(candfeatureVectors)

## FAZER PARA EXEMPLARS ##
exemfeatureVectors = []
for titles in exemplarsTitles:
    featureVector = translateToFeatureVector(scoresList, \
                       titlesList, titles)
    exemfeatureVectors.append(featureVector)

print()
print("Exemplars feature vector")
print(exemfeatureVectors)

    
# create candidates with the info above

candidates = []
for i in range(len(candidatesNames)): 
    candidate = Example(candidatesNames[i], candfeatureVectors[i])
    candidates.append(candidate)

print()
print("Candidates")
for candidate in candidates:
    print(candidate.__str__())


# create exemplars with the info above

exemplars = []
for i in range(len(exemplarsName)):
    exemplar = Example(exemplarsName[i], exemfeatureVectors[i])
    exemplars.append(exemplar)

print()
print("Exemplars")
for exemplar in exemplars:
    print(exemplar.__str__())


## ITS WORKING UNTIL HERE ##

k=6
fileName = "candidates.txt"
try:
    if len(exemplars) != k:
        raise CommandInputError

    clusters = kmeans(candidates, k, True, exemplars)
    print(str(dissimilarity(clusters)))
except CommandInputError:
    print("Command input and input file error: number of initial \
          centroids and k inconsistency between command line and  \
          in file {}".format(fileName))
    
clusters = trykmeans(candidates, k, 6, True)


print()

for cluster in clusters:
    print("antes")
    print(cluster.getCentroid())

    cluster.updateCentroid(getRealCentroid(cluster))

    print("depois")
    print(cluster.getCentroid())