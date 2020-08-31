import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

with open('news_a.json') as json_file:
    data = json.load(json_file)
    for p in data['articles']:
        print(p['published_date'], end=" ")
        print('\t' + p['rank'], end=" ")
        print('\t' + p['title'], end=" ")
        print('\t' + p['link'], end=" ")
        print('')