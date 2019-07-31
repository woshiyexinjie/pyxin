import pydicom

ds = pydicom.dcmread("./rtplan.dcm")  # plan dataset
print(ds.PatientName)
#重新设置患者姓名
ds.PatientName ="testHHHH4"
#获取病人名字
print(ds.PatientName)
print( ds[0x10,0x10])
# print(ds)
#执行 save操作 不然文件不保存
ds.save_as("rtplan.dcm")
