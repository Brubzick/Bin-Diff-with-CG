import angr
from get_functions import GetFunc

p1 = angr.Project('../bin_range/file/file_5.38_x86', auto_load_libs=False)
p2 = angr.Project('../bin_range/file/file_5.38_arm', auto_load_libs=False)

cfg1 = p1.analyses.CFGFast(normalize=True)
size = 0
for node in cfg1.nodes():
    size += node.size
    
funcs = GetFunc(cfg1)

print(len(funcs))