import json
import csv
with open("./news_a.json") as file:
    data = json.load(file)

fname = "output.csv"

with open(fname, "w") as file:
    csv_file = csv.writer(file)
    csv_file.writerow(["Name","Age","Marks","Country"])
    for item in data["articles"]:
        csv_file.writerow([item['author'],item['rights'],item['link'],item['rank']])