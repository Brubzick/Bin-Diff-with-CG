from scipy.optimize import linear_sum_assignment
import numpy as np

def matchedPairs(simMatrix):
    matchedPairs = []

    costMatrix = np.copy(simMatrix)

    for i in range(costMatrix.shape[0]):
        for j in range(costMatrix.shape[1]):
            costMatrix[i,j] = 1 - costMatrix[i,j]

    rowIndex, colIndex = linear_sum_assignment(costMatrix)

    for index in range(len(rowIndex)):
        i = rowIndex[index]
        j = colIndex[index]
        if ((simMatrix[i,j] == max(simMatrix[i,:])) & (simMatrix[i,j] == max(simMatrix[:,j]))):
            matchedPairs.append((i,j,1))
        else:
            matchedPairs.append((i,j,0))

    return matchedPairs

# def matchedPairs(simMatrix):

#     matchedPairs = []
#     if simMatrix.shape[0] <= simMatrix.shape[1]:
#         for i in range(simMatrix.shape[0]):
#             mpi = max(simMatrix[i,:])
#             offset = simMatrix.shape[1]
#             for j in range(simMatrix.shape[1]):
#                 mpj = max(simMatrix[:,j])
#                 simScore = simMatrix[i,j]
#                 if ((simScore == mpi) & (simScore == mpj)):
#                     matchedPair = (i,j,1) # full match
#                     break
#                 elif (simScore == mpi):
#                     if (abs(j-i) < offset):
#                         matchedPair = (i,j,0) # secondary match
#                         offset = abs(j-i)
#             matchedPairs.append(matchedPair)
#     else:
#         for j in range(simMatrix.shape[1]):
#             mpj = max(simMatrix[:,j])
#             offset = simMatrix.shape[0]
#             for i in range(simMatrix.shape[0]):
#                 mpi= max(simMatrix[i,:])
#                 simScore = simMatrix[i,j]
#                 if ((simScore == mpi) & (simScore == mpj)):
#                     matchedPair = (i,j,1) # full match
#                     break
#                 elif (simScore == mpj):
#                     if (abs(i-j) < offset):
#                         matchedPair = (i,j,0) # secondary match
#                         offset = abs(i-j)
#             matchedPairs.append(matchedPair)
    
#     return matchedPairs
        