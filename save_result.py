from openpyxl import Workbook

def saveResult(result, savePath=None):
    if savePath==None:
        savePath = 'result.xlsx'
    
    wb = Workbook()
    ws = wb.active
    for i in range(len(result)):
        for j in range(len(result[i])):
            ws.cell(row=i+1, column=j+1, value=result[i][j])

    wb.save(savePath)

    print('result saved')