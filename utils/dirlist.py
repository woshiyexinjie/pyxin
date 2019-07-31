
import os
#遍历文件目录
path = "./../temp"
files= os.listdir(path)
for file in files:
     if not os.path.isdir(file):
          f = open(path+"/"+file);
          print(f.name)

