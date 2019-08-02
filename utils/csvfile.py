
import csv
import codecs


#  csv的读取
# csvFile = open("instance.csv", "r")
#
# dict_reader = csv.DictReader(csvFile)
#
# for row in dict_reader:
#     print(row.get("TTT"))


# codecs 是自然语言编码转换模块

fileName = 'PythonBook.csv'


with codecs.open(fileName, 'w', 'utf-8') as csvfile:

    filednames = ['书名', '作者']
    writer = csv.DictWriter(csvfile, fieldnames=filednames)

    books = []
    book = {
        'title': '笑傲江湖',
        'author': '金庸',
    }
    title = '西游记'
    auther = '吴承恩'
    book2 = {"title": title, "author": auther}
    books.append(book)
    books.append(book2)

    writer.writeheader()
    for book in books:
        try:
            writer.writerow({'书名':book['title'], '作者':book['author']})
        except UnicodeEncodeError:
            print("编码错误, 该数据无法写到文件中, 直接忽略该数据")