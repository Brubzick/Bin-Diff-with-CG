import angr
from get_functions import GetFunc

p = angr.Project('../bin_range/7zip/24.08/7zzs-arm', auto_load_libs=False)
p2 = angr.Project('../bin_range/7zip/24.08/7zzs-x86', auto_load_libs=False)

cfg = p2.analyses.CFGFast(normalize=True)

funcs = GetFunc(cfg)

for func in funcs:
    if func.name[0:3] != 'sub':
        print(func.name)