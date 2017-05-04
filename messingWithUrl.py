import urllib.request
import os
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
genreId = []

c = 0
for i in procList:
    if i.startswith('product'):
        if i not in productGenred:
            productGenred.add(i)
            print(i.split(':')[1].strip())
            url = 'https://www.amazon.com/dp/' + i.split(':')[1].strip()
            u = urllib.request.Request(url, None, {'User-agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

            opening = urllib.request.urlopen(u).read().decode('utf-8')
            opening = cleanhtml(opening)
            uSplit = opening.split('\n')
            uNoSpace = [line for line in uSplit if line.strip()]

            for k, j in enumerate(uNoSpace):
                if 'Genres' in j:
                    genre = " ".join(uNoSpace[k + 1].split())
                    if 'navmet' in genre:
                        genre = 'No genre available'
                    print(genre)
            print('-'*20)
            c += 1
            genreId.append(genre)


productGenred = list(productGenred)
saver = zip(productGenred, genreId)


saveFile = open(os.path.join('dataProcessed', 'productGenres.txt'), 'w')

for item in saver: #saving to txt with line break
  saveFile.write("%s\n" % item)

