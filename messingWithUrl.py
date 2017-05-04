import urllib.request

import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext




#TODO getting a for cicle here to query every link available and extract at least the genre
'''
url = 'https://www.amazon.com/dp/B008D9NIHW'

u = urllib.request.urlopen(url)

u = u.read().decode('utf-8')

u = cleanhtml(u)

xxx = u.split('\n')

#xxxx = [s for s in xxx if len(s) > 8]

xxxx = [name for name in xxx if name.strip()]


for i,j in enumerate(xxxx):
    if 'Genres' in j:
        print (xxxx[i+1])
        ecsdee = " ".join(xxxx[i + 1].split())
        print(ecsdee)

'''

processed = open('dataProcessed/reviewGreater50.txt', 'r')
processed = processed.read()

procList = processed.split('\n')
productGenred = set()

c = 0
for i in procList:
    if i.startswith('product'):
        if i not in productGenred:
            productGenred.add(i)
            print(i.split(':')[1].strip())
            url = 'https://www.amazon.com/dp/' + i.split(':')[1].strip()
            u = urllib.request.Request(url, None, {'User-agent' : 'Chrome/44.0.2403.107'})

            opening = urllib.request.urlopen(u).read().decode('utf-8')
            opening = cleanhtml(opening)
            uSplit = opening.split('\n')
            uNoSpace = [line for line in uSplit if line.strip()]

            for k, j in enumerate(uNoSpace):
                if 'Genres' in j:
                    genre = " ".join(uNoSpace[k + 1].split())
                    print(genre)
            print('-'*20)
        c += 1
    if (c == 2):
        break