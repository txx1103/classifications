import os, random, shutil

'''
从多级文件夹下随机提取多余指定数目的图片，并且保存在相应的多级文件夹下
'''


def MKD(path):  # 判断目录是否存在，若不存在则新建目录,各级目录一起创建，返回当前以下全部路径
    if not os.path.exists(path):
        os.makedirs(path)
    return path


if __name__ == "__main__":

    data_base_dir = "D:/txx/pytorch/DATA_Prepare/data1/"  # "D:/Desktop/test/valid/"  # 源txt文件夹根路径
    # tarDir = "/media/hdd3/wx/codes/DenseNet-master/test_train1/"  # 移动到一个新的总文件夹
    # if not os.path.exists(tarDir):
    # os.makedirs(tarDir)

    for file in os.listdir(data_base_dir):
        fileDir = data_base_dir + file + '/'  # 取图片的原始路径
        tarDir = MKD(r'D:/txx/pytorch/DATA_Prepare/rand1/' + file + '/')  # 移动到新的文件夹路径，建立相同名称的一二级文件夹
        pathDir = os.listdir(fileDir)
        filenumber = len(pathDir)

        if filenumber > 2:

            picknumber = 500  # lenumber - 400# 所取图片数量
            sample = random.sample(pathDir, picknumber)  # 随机选取picknumber数量的样本图片

            for name in sample:
                # shutil.move(fileDir + name, tarDir + name)  # 移动（剪切）文件
                shutil.copy(fileDir + name, tarDir + name)  # 复制文件

            print('从{}随机抽取了{}份txt文件'.format(fileDir, len(sample)))
