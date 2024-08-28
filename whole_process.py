import angr
import json
import os
import numpy as np
from features import FeaturesExtract
from simMatrix import GetSimMatrix
from result import GetResult
from matched import matchedPairs

def process(p1Path, p2Path, features1Path=None,features2Path=None,simMatrixPath=None,save=False,features1SavePath=None,features2SavePath=None,simMatrixSavePath=None):
    # p1Path and p2Path are required input
    p1 = angr.Project(p1Path, auto_load_libs=False)
    p2 = angr.Project(p2Path, auto_load_libs=False)
    # set threshold for final score according to arch
    if (p1.arch == p2.arch): threshold = 0.75
    else: threshold = 0.6

    filename1 = os.path.basename(p1Path)
    filename2 = os.path.basename(p2Path)

    print('Exracting features')
    # features1
    if features1Path == None:
        features1 = FeaturesExtract(p1)
        if save:
            if features1SavePath == None: features1SavePath = filename1 + '_features1.json'
            with open(features1SavePath, 'w', encoding='utf-8') as f:
                json.dump(features1, f) # save the features
    else:
        with open(features1Path, 'r') as f:
            features1 = json.load(f)
    
    # features2
    if features2Path == None:
        features2 = FeaturesExtract(p2)
        if save:
            if features2SavePath == None: features2SavePath = filename2+'_features2.json'
            with open(features2SavePath, 'w', encoding='utf-8') as f:
                json.dump(features2, f) # save the features
    else:
        with open(features2Path, 'r') as f:
            features2 = json.load(f)
    
    # simMatrix
    if simMatrixPath == None:
        simMatrix = GetSimMatrix(features1, features2)
        if save:
            if simMatrixSavePath == None: simMatrixSavePath = filename1+'_'+filename2+'_simMatrix.json'
            simM_list = simMatrix.tolist()
            with open(simMatrixSavePath, 'w', encoding='utf-8') as f:
                json.dump(simM_list, f) # save the simMatrix
    else:
        with open(simMatrixPath, 'r') as f:
            simMatrix = json.load(f)
        simMatrix = np.array(simMatrix)
    
    # matching and result
    matching = matchedPairs(simMatrix)
    result = GetResult(features1, features2, simMatrix, matching)

    finalScore = result[-1][-1]
    if finalScore > threshold: print('possibly from the same source')

    result.append(['threshold', threshold]) # append threshold info  
    
    return result


    


