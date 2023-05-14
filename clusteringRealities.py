from kMeansClustering import kmeans, readTitlesFile, \
    readCandidatesFile, translateToFeatureVector, \
    Example, dissimilarity
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

candidatesNames, candidatesTitles, \
exemplarsName, exemplarsTitles \
    = readCandidatesFile(candidatesFileName)
# END OF READ FILES

# TRANSLATE FEATURES STRINGS TO SCORES
# Candidates feature vector
candfeatureVectors = []
for titles in candidatesTitles:
    featureVector = translateToFeatureVector(scoresList, \
                       titlesList, titles)
    candfeatureVectors.append(featureVector)

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
    candidate = Example(candidatesNames[i], candfeatureVectors[i])
    candidates.append(candidate)
# END OF CREATE CANDIDATES

# CREATE EXEMPLARS
exemplars = []
for i in range(len(exemplarsName)):
    exemplar = Example(exemplarsName[i], exemfeatureVectors[i])
    exemplars.append(exemplar)
# END OF CREATE EXEMPLARS


## STEP 3 ##
# KMEANS (W/ INITIAL CENTROIDS)
try:
    if len(exemplars) != k:
        raise CommandInputError

    clusters = kmeans(candidates, exemplars, k, True)
    print(str(dissimilarity(clusters)))
except CommandInputError:
    print("Command input and input file error: inconsistency " + \
          "between k and number of initial centroids from " + \
          "command line and file " + \
          "{}, respectively".format(candidatesFileName))
# END OF KMEANS


## STEP 4 ##
# FIND CLUSTERS REAL CENTROIDSP

# END OF FIND CLUSTERS REAL CENTROIDS


## STEP 5 ##
# WRITE OUTPUT FILE

# END OF WRITE OUTPUT FILE