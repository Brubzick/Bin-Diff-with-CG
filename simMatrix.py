from features import FeaturesExtract
from longest_common_part import FindComPart
import numpy as np

def vexCompare(optVexBlock1, optVexBlock2):
    score = 0
    l1 = len(optVexBlock1)
    l2 = len(optVexBlock2)
    for v2 in optVexBlock2:
        mp = 0
        for v1 in optVexBlock1:
            if ((len(v1) == 0) | (len(v2) == 0)):
                tp = 0
            else:
                comPart = FindComPart(v1,v2)
                tp = len(comPart)*2/(len(v1)+len(v2))
            if tp > mp:
                mp = tp
            if mp == 1:
                break
        score += mp

    return (score*2/(l1+l2))



def GetSimMatrix(proj1, proj2):
    features1 = FeaturesExtract(proj1)
    features2 = FeaturesExtract(proj2)

    l1 = len(features1)
    l2 = len(features2)

    nameList1 = []
    nameList2 = []

    for i in range(l1):
        nameList1.append(features1[i]['name'])
    for i in range(l2):
        nameList2.append(features2[i]['name'])

    simM = np.zeros((l1,l2))

    for i in range(l1):
        f1 = features1[i]
        vex1 = f1['optVexBlocks']
        sucNum1 = f1['sucNum']
        preNum1 = f1['preNum']
        for j in range(l2):
            f2 =  features2[j]
            vex2 = f2['optVexBlocks']
            sucNum2 = f1['sucNum']
            preNum2 = f1['preNum']

            vexScore = vexCompare(vex1, vex2)

            if (sucNum1 == sucNum2):
                sucScore = 1
            else:
                sucScore = vexScore*min(sucNum1,sucNum2)/max(sucNum1,sucNum2)

            if (preNum1 == preNum2):
                preScore = 1
            else:
                preScore = vexScore*min(preNum1,preNum2)/max(preNum1,preNum2)

            simM[i,j] = (vexScore+sucScore+preScore)/3
    
    return (nameList1, nameList2, simM)

        
    
        

    

