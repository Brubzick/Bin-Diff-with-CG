import angr
from features import FeaturesExtract
from simMatrix import GetSimMatrix

p1 = angr.Project('../C_bin/dfs_gcc_O0', auto_load_libs=False)
p2 = angr.Project('../C_bin/dfs_gcc2_O0', auto_load_libs=False)

(nameList1, nameList2, simMatrix) = GetSimMatrix(p1,p2)

print(nameList1)
print(nameList2)
# i = nameList1.index('_start')
# j = nameList2.index('_start')
print(simMatrix)


