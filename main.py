import angr
from simMatrix import GetSimMatrix
from matched import matchedPairs
from result import GetResult
import os
from openpyxl import Workbook

p1 = angr.Project('../bin_range/arm/base64_arm', auto_load_libs=False)
p2 = angr.Project('../bin_range/x86/base64_x86', auto_load_libs=False)

filename1 = os.path.basename(p1.filename)
filename2 = os.path.basename(p2.filename)

(features1, features2, simMatrix) = GetSimMatrix(p1,p2)

matching = matchedPairs(simMatrix)

tSize1 = 0
tSize2 = 0
for func in features1:
    tSize1 += func['size']
for func in features2:
    tSize2 += func['size']

result = GetResult(features1, features2, simMatrix, matching)

dataName = filename1+'_'+filename2+'_result.xlsx'
wb = Workbook()
ws = wb.active
for i in range(len(result)):
    for j in range(len(result[i])):
        ws.cell(row=i+1, column=j+1, value=result[i][j])
wb.save('testData/results/'+dataName)



