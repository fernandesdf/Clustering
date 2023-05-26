# 2022-2023 Programacao 2 LTI
# Grupo 031
# 53481 Diogo Alexandre Fernandes Valente
# 54967 Diogo Miguel dos Santos Fernandes

from kMeansClustering import kmeans, trykmeans, \
    readTitlesFile, readCandidatesFile, \
    translateToFeatureVector, Example, dissimilarity, \
    getRealCentroid, processOutputString, writeFile
from CommandInputError import CommandInputError
import sys


## STEP 0 ##
# ARGUMENTS FROM COMMAND LINE
k = int(sys.argv[1])
titlesFileName = sys.argv[2]
candidatesFileName = sys.argv[3]
# END OF ARGUMENTS FROM COMMAND LINE


## STEP 1 ##
# READ FILES
scoresList, titlesList = readTitlesFile(titlesFileName)

candidatesNames, candidatesTitles, candidatesFeatureStr, \
exemplarsName, exemplarsTitles, exemplarsFeatureStr \
    = readCandidatesFile(candidatesFileName)
# END OF READ FILES

# TRANSLATE FEATURES STRINGS TO SCORES
# Candidates feature vector
candfeatureVectors = []
for titles in candidatesTitles:
    featureVector = translateToFeatureVector(scoresList, \
                       titlesList, titles)
    candfeatureVectors.append(featureVector)

if exemplarsName[0] != "void":
    # Exemplars feature vector
    exemfeatureVectors = []
    for titles in exemplarsTitles:
        featureVector = translateToFeatureVector(scoresList, \
                        titlesList, titles)
        exemfeatureVectors.append(featureVector)
# END OF TRANSLATE FEATURES STRINGS TO SCORES


## STEP 2 ##

# CREATE CANDIDATES
candidates = []

for i in range(len(candidatesNames)):

    candidate = Example(candidatesNames[i], \
                        candfeatureVectors[i],\
                        candidatesFeatureStr[i])
    candidates.append(candidate)
# END OF CREATE CANDIDATES

# CREATE EXEMPLARS
if exemplarsName[0] != "void":
    
    exemplars = []
    for i in range(len(exemplarsName)):
        exemplar = Example(exemplarsName[i], \
                           exemfeatureVectors[i], \
                           exemplarsFeatureStr[i])
        exemplars.append(exemplar)
# END OF CREATE EXEMPLARS


## STEP 3 ##
if exemplarsName[0] != "void":
    # KMEANS (W/ INITIAL CENTROIDS)
    try:
        if len(exemplars) != k:
            raise CommandInputError
        
        clusters = kmeans(candidates, k, True, exemplars)
    except CommandInputError:
        print("Command input and input file error: inconsistency " + \
            "between k and number of initial centroids from " + \
            "command line and file " + \
            "{}, respectively".format(candidatesFileName))
        sys.exit()
    # END OF KMEANS
else:
    # TRYKMEANS (WITHOUT INITIAL CENTROIDS)
    clusters = trykmeans(candidates, k, 20, True)
    # END OF TRYKMEANS (WITHOUT INITIAL CENTROIDS)

print()
print("Final cluster: " + str(dissimilarity(clusters)))



## STEP 4 ##
# FIND CLUSTERS REAL CENTROIDS
for cluster in clusters:
    cluster.updateCentroid(getRealCentroid(cluster))
# END OF FIND CLUSTERS REAL CENTROIDS


## STEP 5 ##
# PROCESS STRING TO FILE
outputStr = processOutputString(clusters, k)
# END OF PROCESS STRING TO FILE

# WRITE OUTPUT FILE
writeFile('outputFile.txt', outputStr)
# END OF WRITE OUTPUT FILE