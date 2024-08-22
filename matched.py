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

        