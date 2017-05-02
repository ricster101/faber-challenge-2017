import os


'''
Early draft, way to difficult approach for what was needed
Discarded and given preference to newDataSelector
To be eliminated

c = 0
seeLine = 0
singleReview = []
trustedReviews = []
with open(os.path.join('data', "movies.txt"), encoding="Latin-1") as file:
    for line in file:
        seeLine += 1
        line = line.strip('\n')
        singleReview.append(line)
        c +=1
        if c%9 == 0:
            trusted = False
            if len(singleReview[0]) == 0:
                del singleReview[0]
            den = singleReview[3].split()[1].split('/')[-1]
            ratio = 0
            if not den == '0' and den.isdigit() and '/' in singleReview[3]:
                ratio = eval(singleReview[3].split()[1])
                if ratio >= 0.5:
                    trusted = True

            if trusted:
                trustedReviews.append(singleReview[0])
                trustedReviews.append(singleReview[1])
                trustedReviews.append(ratio)
                trustedReviews.append(singleReview[4])



            singleReview.clear()

saveFile = open(os.path.join('dataProcessed', 'reviewGreater50.txt'), 'w')

for item in trustedReviews:
  saveFile.write("%s\n" % item)

'''