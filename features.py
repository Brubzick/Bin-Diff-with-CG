from get_functions import GetFunc
from vex_opt import VexOpt
from vex_norm import TypeNorm

def FeaturesExtract(proj):
    cfg = proj.analyses.CFGFast(normalize=True)
    funcs = GetFunc(cfg)

    features = []

    for func in funcs:
        featureCollector = {}
        featureCollector['sucNum'] = len(func.suc)
        featureCollector['preNum'] = len(func.pre)
        featureCollector['name'] = func.name

        optVexBlocks = []
        for node in func.nodes:
            optVexNorm = []
            vexBlock = node.block.vex.statements
            optVex = VexOpt(vexBlock)
            
            for vex in optVex:
                optVexNorm.append(TypeNorm(vex))
            
            optVexBlocks.append(optVexNorm)

        featureCollector['optVexBlocks'] = optVexBlocks

        features.append(featureCollector)
    
    return features




