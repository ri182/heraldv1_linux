import json
import csv
with open("news_b_rb.json", encoding="utf-8") as file:
    data = json.load(file)

fname = "output_rb.csv"

with open(fname, "a", encoding="utf-8") as file:
    csv_file = csv.writer(file)
    for item in data["value"]:
        csv_file.writerow([item['datePublished'],item['title'],item['url']])