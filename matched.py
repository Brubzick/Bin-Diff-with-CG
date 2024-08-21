
def matchedPairs(simMatrix):

    matchedPairs = []
    if simMatrix.shape[0] <= simMatrix.shape[1]:
        for i in range(simMatrix.shape[0]):
            mpi = max(simMatrix[i,:])
            offset = simMatrix.shape[1]
            for j in range(simMatrix.shape[1]):
                mpj = max(simMatrix[:,j])
                simScore = simMatrix[i,j]
                if ((simScore == mpi) & (simScore == mpj)):
                    matchedPair = (i,j,1) # full match
                    break
                elif (simScore == mpi):
                    if (abs(j-i) < offset):
                        matchedPair = (i,j,0) # secondary match
                        offset = abs(j-i)
            matchedPairs.append(matchedPair)
    else:
        for j in range(simMatrix.shape[1]):
            mpj = max(simMatrix[:,j])
            offset = simMatrix.shape[0]
            for i in range(simMatrix.shape[0]):
                mpi= max(simMatrix[i,:])
                simScore = simMatrix[i,j]
                if ((simScore == mpi) & (simScore == mpj)):
                    matchedPair = (i,j,1) # full match
                    break
                elif (simScore == mpj):
                    if (abs(i-j) < offset):
                        matchedPair = (i,j,0) # secondary match
                        offset = abs(i-j)
            matchedPairs.append(matchedPair)
    
    return matchedPairs
        

        