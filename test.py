import angr
import networkx

p = angr.Project('../C_bin/dfs_gcc_O0', auto_load_libs=False)

cfg = p.analyses.CFGFast(normalize=True)
cg  = cfg.functions.callgraph

for addr in cg:
    func = cfg.functions.function(addr)
    if func.name == 'DFS': break

func_indentifier = p.analyses.Identifier()
func_indentifier.run()
func_indentifier.map_callsites()