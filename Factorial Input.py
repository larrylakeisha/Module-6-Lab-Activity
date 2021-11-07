# Lakeisha Larry
# November 7, 2021

# Program 3 calculates factorial of user input

import math
n = int(input("Enter a number"))
fact = 1
for n in range(1, n+1):
    fact = fact * n
print("The factorial is : ", end="")
print(fact)

print("Factorial is: ", end="")
print(math.factorial(n))
