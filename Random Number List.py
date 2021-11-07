# Lakeisha Larry
# November 7, 2021

# Program 1 prints 10 random integers between 25 and 35


import random
randomList = []
for i in range(0, 10):
    rnumber = random.randrange(25, 35)
    randomList.append(rnumber)
    print(i + 1, "Random Number = ", rnumber)
print(randomList)
