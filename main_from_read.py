import json
from openpyxl import Workbook
import numpy as np
from matched import matchedPairs
from result import GetResult

filename1 = 'dfs_gcc_O0'
filename2 = 'hello_gcc_O0'

with open('./testData/features/'+filename1+'_features.json','r') as f:
    features1 = json.load(f)

with open('./testData/features/'+filename2+'_features.json','r') as f:
    features2 = json.load(f)

with open('./testData/simMatrixes/'+filename1+'_'+filename2+'_simMatrix.json','r') as f:
    simMatrix = json.load(f)

simMatrix = np.array(simMatrix)
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
wb.save('./testData/results/'+dataName)