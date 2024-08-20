import angr
from simMatrix import GetSimMatrix
from matched import matchedPairs

p1 = angr.Project('../bin_range/file/file_5.38_x86', auto_load_libs=False)
p2 = angr.Project('../bin_range/file/file_5.38_arm', auto_load_libs=False)

(nameList1, nameList2, simMatrix) = GetSimMatrix(p1,p2)

matching = matchedPairs(simMatrix)

scoreList = []
for site in matching:
    print(nameList1[site[0]], nameList2[site[1]], simMatrix[site[0],site[1]])
    scoreList.append(simMatrix[site[0],site[1]])

finalScore = (sum(scoreList)/len(scoreList))*((len(matching)/simMatrix.shape[0])+(len(matching)/simMatrix.shape[1]))/2
print(finalScore)








