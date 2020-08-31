import json
import csv
with open("./news_b_ks.json") as file:
    data = json.load(file)

fname = "output_ks.csv"

with open(fname, "a") as file:
    csv_file = csv.writer(file)
    csv_file.writerow(["Time","Title","URL"])
    for item in data["value"]:
        csv_file.writerow([item['datePublished'],item['title'],item['url']])