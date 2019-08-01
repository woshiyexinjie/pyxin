
import csv

csvFile = open("instance.csv", "r")

dict_reader = csv.DictReader(csvFile)

for row in dict_reader:
    print(row.get("TTT"))
