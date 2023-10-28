import numpy as np
import pandas as pd

data = pd.read_excel(r"D:/WX/Desktop/data.xlsx",header=None)
desktop_path = "D://WX//Desktop//fenlei//"
count = 0
# 获取所有的列数
clo = data.columns.size
data1 = data.iloc[:, 0]
data1_da = data1.values.tolist()

for i in [x for x in range(clo) if x != 0]:
    data2 = data.iloc[:, i]
    data2_da= data2.values.tolist()
    full_path = desktop_path + "blxw_" + str(count) + '.txt'
    file = open(full_path, 'w')
    # 写入的内容：
    with open(full_path, "a") as f:

        for data_len in range(len(data1_da)):
            print("data1_da[i]的值%d",data1[data_len])
            f.write('{:}:{:}\n'.format(data1_da[data_len], data2_da[data_len]))
        f.close()

    count += 1


