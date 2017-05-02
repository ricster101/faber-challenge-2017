import os


c = 0
with open(os.path.join('data', "movies.txt")) as file:
    for line in file:
        print(line)
        c +=1
        if c%9 == 0:
            breaker = input("Press Enter to continue, type X to close...")
            print("\n" * 100)
            if breaker == 'X' or breaker == 'x':
                break
