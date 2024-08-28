
class Func:
    def __init__(self, name, addr):
        self.suc = []
        self.pre = []
        self.cfg = None
        self.name = name
        self.addr = addr

# 根据控制流图和调用图提取出函数和函数中有效的基本块
def GetFunc(cfg):

    cg = cfg.functions.callgraph
    addrs = cg.nodes
    edges = cg.edges
    funcDict = {}

    for addr in addrs:
        func = cfg.functions.function(addr)
        if (not func.is_simprocedure):
            cfgNodes = []
            for node in func.nodes:
                if hasattr(node, 'is_hook'):
                    if (not node.is_hook):
                        cfgNode = cfg.get_any_node(node.addr)
                        if cfgNode != None:
                            cfgNodes.append(cfgNode)
            
            if (len(cfgNodes) > 0):
                subCFG = cfg.graph.subgraph(cfgNodes) # CFG (networkx Digraph) of the function
                f = Func(func.name, func.addr)
                f.cfg = subCFG
                funcDict[addr] = f
    
    for edge in edges:
        parent = edge[0]
        son = edge[1]
        if ((funcDict.get(parent)!=None) & (funcDict.get(son)!=None)):
            funcDict[parent].suc.append(funcDict[son])
            funcDict[son].pre.append(funcDict[parent])

    funcs = []
    for func in funcDict.values():
        funcs.append(func)

    return funcs

    