
def matchedPairs(simMatrix):

    matchedPairs = []
    if simMatrix.shape[0] <= simMatrix.shape[1]:
        for i in range(simMatrix.shape[0]):
            mpi = max(simMatrix[i,:])
            for j in range(simMatrix.shape[1]):
                mpj = max(simMatrix[:,j])
                simScore = simMatrix[i,j]
                if ((simScore == mpi) & (simScore == mpj)):
                    matchedPairs.append((i,j))
                    break
    else:
        for j in range(simMatrix.shape[1]):
            mpj = max(simMatrix[:,j])
            for i in range(simMatrix.shape[0]):
                mpi= max(simMatrix[i,:])
                simScore = simMatrix[i,j]
                if ((simScore == mpi) & (simScore == mpj)):
                    if (i,j) not in matchedPairs:
                        matchedPairs.append((i,j))
                        break
    
    return matchedPairs
        

        