from features import FeaturesExtract
from longest_common_part import FindComPart
import numpy as np
import os
import json
import sys

def vexMnemonic(optVexBlock1, optVexBlock2):# count mnemonic to calculate similarity
    mDict1 = {}
    mDict2 = {}
    for block in optVexBlock1:
        for mnemonic in block:
            if mDict1.get(mnemonic):
                mDict1[mnemonic] += 1
            else:
                mDict1[mnemonic] = 1
    for block in optVexBlock2:
        for mnemonic in block:
            if mDict2.get(mnemonic):
                mDict2[mnemonic] += 1
            else:
                mDict2[mnemonic] = 1
    
    mnemonics = set(mDict1.keys()).union(mDict2.keys())
    if len(mnemonics) == 0:
        return 1

    f = 0
    for mnemonic in mnemonics:
        if ((mDict1.get(mnemonic)!=None) & (mDict2.get(mnemonic)!=None)):
            c1 = mDict1.get(mnemonic)
            c2 = mDict2.get(mnemonic)
            f += min(c1,c2)/max(c1,c2)
    
    vexScore = f/len(mnemonics)
    return vexScore
    

def vexCompare(optVexBlock1, optVexBlock2):
    score = 0
    l1 = len(optVexBlock1)
    l2 = len(optVexBlock2)
    for v2 in optVexBlock2:
        mp = 0
        for v1 in optVexBlock1:
            if ((len(v1) == 0) & (len(v2) == 0)):
                tp = 1
            elif ((len(v1) == 0) | (len(v2) == 0)):
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

def GetSimMatrix(proj1, proj2, vexMode='Mnemonic'):
    print('exracting features')
    filename1 = os.path.basename(proj1.filename)
    filename2 = os.path.basename(proj2.filename)
    features1 = FeaturesExtract(proj1)
    features2 = FeaturesExtract(proj2)

    l1 = len(features1)
    l2 = len(features2)
    total = l1*l2

    simM = np.zeros((l1,l2))
    print('start comparing')
    count = 0
    for i in range(l1):
        f1 = features1[i]
        vex1 = f1['optVexBlocks']
        sucNum1 = f1['sucNum']
        preNum1 = f1['preNum']
        name1 = f1['name']
        bN1 = f1['bN']
        for j in range(l2):
            f2 =  features2[j]
            vex2 = f2['optVexBlocks']
            sucNum2 = f1['sucNum']
            preNum2 = f1['preNum']
            name2 = f2['name']
            bN2 = f2['bN']

            if vexMode == 'Mnemonic':
                vexScore = vexMnemonic(vex1, vex2)
            elif vexMode == 'vexCompare':
                vexScore = vexCompare(vex1, vex2)
            else:
                print('Wrong parameter for vexMode')
                sys.exit(1)

            if (sucNum1 == sucNum2):
                sucScore = 1
            else:
                sucScore = 0

            if (preNum1 == preNum2):
                preScore = 1
            else:
                preScore = 0

            if (name1 == name2):
                nScore = 1
            else:
                nScore = 0
            
            if (bN1 == bN2):
                bNScore = 1
            else:
                bNScore = min(bN1,bN2)/max(bN1,bN2)

            simM[i,j] = (sucScore*0.1 + preScore*0.1 + nScore*0.2 + bNScore*0.2 + vexScore*0.4)
            
            count += 1
            progress = count/total*100
            print('progress:',f'{progress}%',end='\r')
    
    dataName = filename1+'_'+filename2+'_simMatrix.json'
    simM_list = simM.tolist()
    with open('testData/simMatrixes/'+dataName, 'w', encoding='utf-8') as f:
        json.dump(simM_list, f) # save the simMatrix
    
    return (features1, features2, simM)


