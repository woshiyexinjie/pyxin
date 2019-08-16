
import csv
import codecs


#  csv的读取
csvFile = open("PythonBook.csv", "r")

dict_reader = csv.DictReader(csvFile)

for row in dict_reader:
    print(row)
    row['作者'] = 'HEl'
    row.update()
with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})



# codecs 是自然语言编码转换模块
# fileName = 'PythonBook.csv'
#
#
# with codecs.open(fileName, 'w', 'utf-8') as csvfile:
#
#     filednames = ['书名', '作者']
#     writer = csv.DictWriter(csvfile, fieldnames=filednames)
#
#     books = []
#     book = {
#         'title': '笑傲江湖',
#         'author': '金庸',
#     }
#     title = '西游记'
#     auther = '吴承恩'
#     book2 = {"title": title, "author": auther}
#     books.append(book)
#     books.append(book2)
#
#     writer.writeheader()
#     for book in books:
#         try:
#             writer.writerow({'书名':book['title'], '作者':book['author']})
#         except UnicodeEncodeError:
#             print("编码错误, 该数据无法写到文件中, 直接忽略该数据")