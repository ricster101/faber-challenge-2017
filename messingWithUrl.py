import urllib.request

import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext




#TODO getting a for cicle here to query every link available and extract at least the genre

url = 'https://www.amazon.com/dp/B000ICXQHY'

u = urllib.request.urlopen(url)

u = u.read().decode('utf-8')

u = cleanhtml(u)

xxx = u.split('\n')

#xxxx = [s for s in xxx if len(s) > 8]

xxxx = [name for name in xxx if name.strip()]


for i,j in enumerate(xxxx):
    if 'Genres' in j:
        print (xxxx[i+1])
