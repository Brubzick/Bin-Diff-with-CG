from get_functions import GetFunc
from vex_opt import VexOpt
from vex_norm import TypeNorm
import networkx

# 抽取特征，得到一个元素都为字典的列表
def FeaturesExtract(proj):
    pCFG = proj.analyses.CFGFast(normalize=True)
    funcs = GetFunc(pCFG)

    proj.analyses.CompleteCallingConventions(recover_variables=True, cfg=pCFG.model)

    features = []

    for func in funcs:
        name = func.name
        cfg = func.cfg
        nodes = cfg.nodes

        featureCollector = {}
        featureCollector['sucNum'] = len(func.suc)
        featureCollector['preNum'] = len(func.pre)
        featureCollector['name'] = name
        featureCollector['bN'] = len(nodes)
        featureCollector['density'] = networkx.density(cfg)
        featureCollector['meanDegree'] = sum(d for _,d in cfg.degree)/len(nodes)
        featureCollector['transitivity'] = networkx.transitivity(cfg)
        featureCollector['diameter'] = max(networkx.diameter(networkx.subgraph(cfg, x).to_undirected())
                                                             for x in list(networkx.connected_components(cfg.to_undirected())))
        featureCollector['cyclomaticComplexity'] = len(cfg.edges) - len(nodes) + 2*len([c for c in networkx.weakly_connected_components(cfg)])

        # 判断函数名是否是地址
        hexAddr = str(hex(func.addr))[2:]
        if (hexAddr in name): featureCollector['goodName'] = False
        else: featureCollector['goodName'] = True

        optVexBlocks = []
        size = 0
        for node in nodes:
            size += node.size
            optVexNorm = []
            vexBlock = node.block.vex.statements
            optVex = VexOpt(vexBlock)
            
            for vex in optVex:
                optVexNorm.append(TypeNorm(vex))
            
            optVexBlocks.append(optVexNorm)
        mDict = {}
        for block in optVexBlocks:
            for mnemonic in block:
                if mDict.get(mnemonic):
                    mDict[mnemonic] += 1
                else:
                    mDict[mnemonic] = 1
        featureCollector['mnemonics'] = mDict

        featureCollector['size'] = size

        # 函数的参数
        # conv = proj.analyses.CallingConvention(func=func,cfg=pCFG.model,analyze_callsites=True)
        # a = proj.analyses.VariableRecoveryFast(func=func)
        # dec = proj.analyses.Decompiler(func=func,cfg=pCFG.model)
        # arguments = func.prototype.args
        # ret = func.prototype.returnty
        # featureCollector['args'] = arguments
        # featureCollector['ret'] = ret

        features.append(featureCollector)

    return features




