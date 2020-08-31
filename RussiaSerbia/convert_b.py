import json
import sys
import requests

with open('news_b.json') as json_file:
    data = json.load(json_file)
    for p in data['value']:
        print(p['datePublished'], end=" ")
        print('\t' + p['title'], end=" ")
        print('\t' + p['url'], end=" ")
        print('')