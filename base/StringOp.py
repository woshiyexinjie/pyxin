
mstr = "2019"
cpmpareDate = "2017"
if(mstr > cpmpareDate):
    print(mstr)
    print("开始处理这个字符串")
    yearDc = int(mstr[0:4])
    #减去 2
    newYearDc = yearDc -2;
    print(newYearDc)
    mstr.replace("2019","2017")
    print(str(newYearDc)+mstr[4:])