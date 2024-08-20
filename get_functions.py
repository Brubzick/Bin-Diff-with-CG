
class Func:
    def __init__(self, name):
        self.suc = []
        self.pre = []
        self.nodes = []
        self.name = name

def GetFunc(cfg):

    cg = cfg.functions.callgraph

    addrs = cg.nodes
    edges = cg.edges
    funcDict = {}

    for addr in addrs:
        func = cfg.functions.function(addr)
        if (not func.is_simprocedure):
            blocks = []
            nodes = func.nodes
            for n in nodes:
                if hasattr(n, 'is_hook'):
                    if (not n.is_hook):
                        blocks.append(cfg.get_any_node(n.addr))
            if (len(blocks) == 0):
                continue
            elif ((len(blocks) == 1) & (len(blocks[0].block.vex.statements) <= 1)):
                continue
            else:
                f = Func(func.name)
                f.nodes = blocks
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

    