import os
from whole_process import process
from save_result import saveResult

if __name__ == '__main__':
    # required parameters 二进制文件路径
    file1Path = '../bin_range/unzip/unzip_x86'
    file2Path = '../bin_range/file/file_5.38_x86'
    filename1 = os.path.basename(file1Path)
    filename2 = os.path.basename(file2Path)
    # optional parameters 
    # 如果提供特征和相似度矩阵，则提供的部分将不会再计算
    features1Path = None
    features2Path = None
    simMatrixPath = None
    # 是否保存抽取的特征和相似度矩阵，如果是已提供的，则不会保存
    save = False
    features1SavePath = './testData/features/'+filename1+'_features.json'
    features2SavePath = './testData/features/'+filename2+'_features.json'
    simMatrixSavePath = './testData/simMatrixes/'+filename1+'_'+filename2+'_simMatrix.json'

    # 是否保存结果和保存路径
    resultSave = False
    resultSavePath = './testData/results/'+filename1+'_'+filename2+'_result.xlsx'
    
    result = process(p1Path=file1Path, p2Path=file2Path, features1Path=features1Path, features2Path=features2Path, simMatrixPath=simMatrixPath, save=save, features1SavePath=features1SavePath, features2SavePath=features2SavePath, simMatrixSavePath=simMatrixSavePath)
    
    if resultSave:
        saveResult(result, resultSavePath)