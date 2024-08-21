import angr

p1 = angr.Project('../bin_range/openssl/openssl_x86', auto_load_libs=False)
cfg = p1.analyses.CFGFast(normalize=True)

cg = cfg.functions.callgraph

addrs = cg.nodes

addr = list(addrs)[2]

func = cfg.functions.function(addr)

for node in func.nodes:
    print(cfg.get_any_node(node.addr))