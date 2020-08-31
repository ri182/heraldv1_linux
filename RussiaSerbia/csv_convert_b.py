import json
import csv
with open("./news_b_ru.json") as file:
    data = json.load(file)

fname = "output_rs.csv"

with open(fname, "a") as file:
    csv_file = csv.writer(file)
    for item in data["value"]:
        csv_file.writerow([item['datePublished'],item['title'],item['url']])