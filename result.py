
def GetResult(features1, features2, simMatrix, matching, goodName):

    tSize1 = 0
    tSize2 = 0
    for func in features1:
        tSize1 += func['size']
    for func in features2:
        tSize2 += func['size']

    scoreList = []
    size1 = 0
    size2 = 0
    result = []
    row = ['function1','size1','function2','size2','simMatrix']
    print(row)
    result.append(row)
    for site in matching: # only full match with good name (not named by address) is printed, but secondary match is also used for final score calcaulation.
        if site[2] == 1:
            f1 = features1[site[0]]
            f2 = features2[site[1]]
            if goodName:
                if (f1['goodName'] or f2['goodName']):
                    row = [f1['name'], f1['size'], f2['name'], f2['size'], simMatrix[site[0],site[1]]]
                    print(row)
                    result.append(row)
            else:
                row = [f1['name'], f1['size'], f2['name'], f2['size'], simMatrix[site[0],site[1]]]
                print(row)
                result.append(row)
                
        scoreList.append(simMatrix[site[0],site[1]])
        size1 += features1[site[0]]['size']
        size2 += features2[site[1]]['size']

    finalScore = (sum(scoreList)/len(scoreList))*((size1/tSize1)+(size2/tSize2))/2
    print('Final Score:',finalScore)
    print(size1,tSize1,size2,tSize2)

    result.append(['finalScore', finalScore])
    return result
