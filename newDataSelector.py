import os


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
            for j in singleReview:
                trusted = False
                ratio = 0
                if j.startswith('review/helpfulness:'):
                    den = j.split()[1].split('/')[-1]
                    if not den == '0' and den.isdigit():
                        ratio = eval(j.split()[1])
                        if ratio >= 0.5:
                            trusted = True
                if j.startswith('product/productId'):
                    product = j
                if j.startswith('review/userId'):
                    user = j
                if j.startswith('review/score'):
                    score = j

            if trusted:
                trustedReviews.append(product)
                trustedReviews.append(user)
                trustedReviews.append(ratio)
                trustedReviews.append(score)



            singleReview.clear()

saveFile = open(os.path.join('dataProcessed', 'reviewGreater50.txt'), 'w')

for item in trustedReviews:
  saveFile.write("%s\n" % item)
