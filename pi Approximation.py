# Lakeisha Larry
# November 7, 2021

# Program 1 calculates pi approximation

import math

# Initialize denominator
k = 1

# Initialize sum
s = 0

for i in range(1000000):
    if i % 2 == 0:
        s += 4 / k
    else:
        s -= 4 / k
    k += 2

print(s)
print(math.pi)
