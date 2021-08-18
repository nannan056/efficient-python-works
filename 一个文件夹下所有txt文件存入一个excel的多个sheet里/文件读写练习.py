import os
import pandas as pd

writer = pd.ExcelWriter("my_excel.xls", engine='openpyxl')
num = 1

for root, dirs, files in os.walk('./TXT转excel'):  
    print(root) #当前目录路径  
    print(dirs) #当前路径下所有子目录  
    print(files) #当前路径下所有非目录子文件
    for file in files:
        tmp=pd.read_csv("./TXT转excel/%s"%(file),sep=',')
        tmp.to_excel(excel_writer=writer, sheet_name=file)
    writer.save()


# for sheet_name in sheet_names:
#         # 下面的保存文件处填写writer，结果会不断地新增sheet，避免循环时被覆盖
#     report_dict[sheet_name].to_excel(excel_writer=writer, sheet_name=sheet_name, encoding="GBK")
#     print(sheet_name + "  保存成功！共%d个，这个 sheet 是第%d个。" % (len(sheet_names), num))
#     num += 1
# writer.save()
