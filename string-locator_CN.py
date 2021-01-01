# Python version: python3.x
# Coding: UTF-8


import linecache
import os


# 确定当前操作系统路径分隔符
osName = os.name
if osName == "posix":
	pathSeparator = "/"
elif osName == "nt":
	pathSeparator = "\\"

# 主程序
while True:
    cwd = os.getcwd()+pathSeparator
    print("当前绝对路径: "+cwd)
    filePath = input("输入文件路径(绝对/相对): ")
    # 判断是否绝对路径.如果否,转换为绝对路径
    while os.path.isabs(filePath) == False:
        filePath = cwd+filePath
        # 判断路径是否存在.如果否,重新输入
        while os.path.exists(filePath) == False:
            filePath = input("文件未找到.\n"
            	             "请重新输入文件路径: ")
            # 判断路径是否文件.如果否,重新输入
            while os.path.isfile(filePath) == False:
                filePath = input("输入的路径不是文件.\n请重新输入文件路径: ")

            else:
                pass
        else:
            pass
    else:
        pass 
    string = input("输入要查找的字符串: ")

    # 获取文件行数
    count=0
    f = open(filePath, "r")
    for line in f.readlines():
        count=count+1
    f.close()

    # 开始查找
    line = 1
    while line != count+1:
        theLine = linecache.getline(filePath, line)
        if string in theLine:
            print("第 "+str(line)+" 行已找到.\n")
            print("行数: "+str(line))
            print("该行内容: "+theLine)
        elif line == count:
            print("未找到该字符串.")
            break
        else:
            print("第 "+str(line)+" 行未找到...")
            line = line + 1
