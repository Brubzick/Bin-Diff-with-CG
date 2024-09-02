import numpy as np

def vexMnemonic(mnemonics1, mnemonics2):# count mnemonic to calculate similarity
   
    mnemonics = set(mnemonics1.keys()).union(mnemonics2.keys())
    if len(mnemonics) == 0:
        return 1

    f = 0
    for mnemonic in mnemonics:
        if ((mnemonics1.get(mnemonic)!=None) & (mnemonics2.get(mnemonic)!=None)):
            c1 = mnemonics1.get(mnemonic)
            c2 = mnemonics2.get(mnemonic)
            f += min(c1,c2)/max(c1,c2)
    
    vexScore = f/len(mnemonics)
    return vexScore

# get similarity matrix 相似度矩阵
def GetSimMatrix(features1, features2):
    """
    目前有的特征：
    sucNum
    preNum
    name
    bN
    density
    meanDegree
    transitivity
    diameter
    cyclomaticComplexity
    mnemonics
    size
    """
    l1 = len(features1)
    l2 = len(features2)
    total = l1*l2

    simM = np.zeros((l1,l2))
    print('Start computing simMatrix')
    count = 0
    for i in range(l1):
        f1 = features1[i]
        sucNum1 = f1['sucNum']
        preNum1 = f1['preNum']
        name1 = f1['name']
        bN1 = f1['bN']
        den1 = f1['density']
        mD1 = f1['meanDegree']
        tran1 = f1['transitivity']
        dia1 = f1['diameter']
        cC1 = f1['cyclomaticComplexity']
        for j in range(l2):
            f2 =  features2[j]
            sucNum2 = f1['sucNum']
            preNum2 = f1['preNum']
            name2 = f2['name']
            bN2 = f2['bN']
            den2 = f2['density']
            mD2 = f2['meanDegree']
            tran2 = f2['transitivity']
            dia2 = f2['diameter']
            cC2 = f2['cyclomaticComplexity']

            # vexScore
            vexScore = vexMnemonic(f1['mnemonics'], f2['mnemonics'])

            # sucScore
            if (sucNum1 == sucNum2): sucScore = 1               
            else: sucScore = 0               

            # preScore
            if (preNum1 == preNum2): preScore = 1               
            else: preScore = 0                
            
            # name score
            if (name1 == name2): nScore = 1                
            else: nScore = 0                
            
            # basic block number score
            bNScore = min(bN1,bN2)/max(bN1,bN2)

            # density score, meanDegree score, transitivity score, diameter score and cyclpmaticComplexity score
            if ((den1 == 0) and (den2 == 0)):denScore = 1
            else: denScore = min(den1, den2)/max(den1,den2)

            if ((mD1 == 0) and (mD2 == 0)): mDScore = 1  
            else: mDScore = min(mD1,mD2)/max(mD1,mD2)

            if ((tran1 == 0) and (tran2 == 0)): tranScore = 1
            else: tranScore = min(tran1,tran2)/max(tran1, tran2)

            if ((dia1 == 0) and (dia2 == 0)): diaScore = 1                
            else: diaScore = min(dia1,dia2)/max(dia1,dia2)

            if ((cC1 == 0) and (cC2 == 0)): cCScore = 1
            else: cCScore = min(cC1,cC2)/max(cC1,cC2)          
            
            # score in similarity matrix
            simM[i,j] = (sucScore + preScore)*0.1/2 + nScore*0.1 + bNScore*0.1 + vexScore*0.3 + (denScore + mDScore + tranScore + diaScore + cCScore)*0.4/5
            
            count += 1
            progress = count/total*100
            print('progress:',f'{progress:.4f}%',end='\r')
    
    return simM