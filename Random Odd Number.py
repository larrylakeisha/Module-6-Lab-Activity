# Lakeisha Larry
# November 7, 2021

# Program 2 prints an odd integer between the numbers 0 and 100

import random
'''What if the generated number is not odd number?'''
oddnum = random.randrange(1, 100)
if oddnum % 2 != 0:
    print(oddnum)
