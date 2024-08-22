import angr
from simMatrix import GetSimMatrix
from matched import matchedPairs
from result import GetResult
import os
from openpyxl import Workbook

p1 = angr.Project('../bin_range/ssh/ssh_x86', auto_load_libs=False)
p2 = angr.Project('../bin_range/openssl/openssl_x86', auto_load_libs=False)

if p1.arch == p2.arch:
    threshold = 0.75
else:
    threshold = 0.6

filename1 = os.path.basename(p1.filename)
filename2 = os.path.basename(p2.filename)

(features1, features2, simMatrix) = GetSimMatrix(p1,p2,vexMode='Mnemonic') # vexMode默认为'Mnemonic',还可以改为'vexCompare',但会大大增加运行时间，且不一定会增加结果的精确度。

matching = matchedPairs(simMatrix)

tSize1 = 0
tSize2 = 0
for func in features1:
    tSize1 += func['size']
for func in features2:
    tSize2 += func['size']

result = GetResult(features1, features2, simMatrix, matching)

finalScore = result[-1][-1]

dataName = filename1+'_'+filename2+'_result.xlsx'
wb = Workbook()
ws = wb.active
for i in range(len(result)):
    for j in range(len(result[i])):
        ws.cell(row=i+1, column=j+1, value=result[i][j])
wb.save('testData/results/'+dataName)

if finalScore > threshold:
    print('possibly be the same source.')