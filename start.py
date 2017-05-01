import os

with open(os.path.join('data', "movies.txt")) as infile:
    for line in infile:
        print(line)
