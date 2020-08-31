import unittest
import sys
import json
from GoogleNews import GoogleNews
googlenews = GoogleNews(lang='en')

googlenews.setlang('en')
googlenews.search('Serbia')
googlenews.getpage(1)

data = googlenews.result()

text_file = open("news_c_rs.json", "w")
text_file.write(json.dumps(data))
text_file.close()
