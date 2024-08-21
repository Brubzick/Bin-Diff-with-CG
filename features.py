from get_functions import GetFunc
from vex_opt import VexOpt
from vex_norm import TypeNorm
import os
import json

def FeaturesExtract(proj):
    filename = os.path.basename(proj.filename)
    cfg = proj.analyses.CFGFast(normalize=True)
    funcs = GetFunc(cfg)

    features = []

    for func in funcs:
        featureCollector = {}
        featureCollector['sucNum'] = len(func.suc)
        featureCollector['preNum'] = len(func.pre)
        featureCollector['name'] = func.name
        featureCollector['bN'] = len(func.nodes)

        optVexBlocks = []
        size = 0
        for node in func.nodes:
            size += node.size
            optVexNorm = []
            vexBlock = node.block.vex.statements
            optVex = VexOpt(vexBlock)
            
            for vex in optVex:
                optVexNorm.append(TypeNorm(vex))
            
            optVexBlocks.append(optVexNorm)

        featureCollector['optVexBlocks'] = optVexBlocks
        featureCollector['size'] = size

        features.append(featureCollector)

    dataName = filename + '_features.json'
    with open('testData/features/'+dataName, 'w', encoding='utf-8') as f:
        json.dump(features, f) # save the features
    
    return features




