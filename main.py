from kMeansClustering import kmeans, trykmeans, Example, \
    dissimilarity, readCandidatesFile, writeFile, \
    translateToFeatureVector, readTitlesFile
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

class Candidate(Example):
    def __init__(self, name, features, label=None): # e aqui tbm
        # (passar os titles com os nomes em macho femea?)
        super().__init__(name, features, label)
        #adicionar campos necessarios
        #titles = titles 

#rita = Candidate("Rita", examplesList, titlesList)

# ****** |1st Tests| ******

# rita = Example("Rita", [8, 6, 9, 6, 5, 5])
# julio = Example("Julio", [9, 10, 8, 8, 9, 4])
# cesar = Example("Cesar", [7, 10, 0, 0, 0, 0])
# paulo = Example("Paulo", [11, 0, 11, 11, 0, 0])


# examplesList = [rita, julio, cesar, paulo]
# k=2 # number of groups
# #clusters = kmeans(examplesList, k, True)

# t = 5 # number of tries
# clustersTryKMeans = trykmeans(examplesList, k, t, True)
# dissim = dissimilarity(clustersTryKMeans)

# print(clustersTryKMeans[0])
# print(clustersTryKMeans[1])
# print(dissim)

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

# com dic, tem o problema do titulo ter genero... 
# como eh q vou distinguir..
# dic = readTitlesFile('titles.txt')
# print("dic scoresList")
# print(dic)


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

    
## ITS WORKING UNTIL HERE ##


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

# ISTO N DEVE SER NECESSARIO, O PROF TBM N UTILIZOU
ola = exemplars[1].getFeatures()
print()
print(ola)
print(exemplars[0].__eq__(exemplars[0]))