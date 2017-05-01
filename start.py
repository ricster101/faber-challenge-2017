import os


c = 0
singleReview = []
with open(os.path.join('data', "movies.txt")) as file:
    for line in file:
        print(line)
        singleReview.append(line)
        c +=1
        if c%9 == 0:
            print(singleReview)
            singleReview.clear()
            breaker = input("Press Enter to continue, type X to close...")
            if breaker == 'X' or 'x':
                break
            print("\n" * 100)