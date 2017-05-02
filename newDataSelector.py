import os


c = 0
singleReview = []
trustedReviews = []
with open(os.path.join('data', "movies.txt"), encoding="Latin-1") as file: #enconding problems in some bytes
    for line in file:
        line = line.strip('\n') #getting rid of line breaks
        singleReview.append(line) #getting a single review from the file
        c +=1
        if c%9 == 0: #each single review has 9 lines
            for j in singleReview:
                trusted = False
                ratio = 0
                if j.startswith('review/helpfulness:'): #ratio of people who were helped by the review
                    den = j.split()[1].split('/')[-1]
                    if not den == '0' and den.isdigit(): #getting rid of the 0/0 cases
                        ratio = eval(j.split()[1])
                        if ratio >= 0.5: #selecting only reviews with more the 50% help ration
                            trusted = True
                if j.startswith('product/productId'): #getting prod ID
                    product = j
                if j.startswith('review/userId'): #getting user ID
                    user = j
                if j.startswith('review/score'): #getting review score
                    score = j

            if trusted: #assembly of the trusted review list
                trustedReviews.append(product)
                trustedReviews.append(user)
                trustedReviews.append(ratio)
                trustedReviews.append(score)



            singleReview.clear()

saveFile = open(os.path.join('dataProcessed', 'reviewGreater50.txt'), 'w')

for item in trustedReviews: #saving to txt with line break
  saveFile.write("%s\n" % item)
