import shutil
import os

# 源文件夹列表
source_folders = ['D:/txx/pytorch/DATA_Prepare/rand1/7.1 归一化',
                  'D:/txx/pytorch/DATA_Prepare/rand1/7.2 归一化',
                  'D:/txx/pytorch/DATA_Prepare/rand1/7.3 归一化',
                  'D:/txx/pytorch/DATA_Prepare/rand1/7.4 归一化',
                  'D:/txx/pytorch/DATA_Prepare/rand1/7.5 归一化',
                  'D:/txx/pytorch/DATA_Prepare/rand1/7.6 归一化',
                  'D:/txx/pytorch/DATA_Prepare/rand1/7.7 归一化',
                  'D:/txx/pytorch/DATA_Prepare/rand1/7.8 归一化',
                  'D:/txx/pytorch/DATA_Prepare/rand1/7.9 归一化',
                  'D:/txx/pytorch/DATA_Prepare/rand1/7.10 归一化',
                  ]

# 目标文件夹
target_folder = 'D:/txx/pytorch/DATA_Prepare/new_data/7'

# 遍历每个源文件夹，并将其内容复制到目标文件夹中
for source_folder in source_folders:
    # 构建源文件夹的完整路径
    source_folder_path = os.path.join(source_folder)

    # 获取源文件夹中的所有文件和子文件夹
    folder_contents = os.listdir(source_folder_path)

    # 遍历源文件夹中的文件和子文件夹
    for item in folder_contents:
        # 构建源文件或子文件夹的完整路径
        item_path = os.path.join(source_folder_path, item)

        # 构建目标路径，将源文件夹的内容复制到目标文件夹中
        target_path = os.path.join(target_folder, item)

        # 如果是文件，则使用shutil复制文件
        if os.path.isfile(item_path):
            shutil.copy(item_path, target_path)
        # 如果是文件夹，则使用shutil复制整个文件夹及其内容
        elif os.path.isdir(item_path):
            shutil.copytree(item_path, target_path)

print("复制完成")
