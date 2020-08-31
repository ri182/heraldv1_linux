import json
import csv
with open("./news_c_rs.json") as file:
    data = json.load(file)

fname = "output_srz.csv"

with open(fname, "a") as file:
    csv_file = csv.writer(file)
    for item in data:
        csv_file.writerow([item['date'],item['title'],item['link']])