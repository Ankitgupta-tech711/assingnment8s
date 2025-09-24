#TASK 1

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter the number: "))
result = factorial(n)
print('factorial of 5 is: ',result)

#TASK 2

import math
n=int(input('Enter the number:'))
print('square root:',math.sqrt(n))
print('logarithm:',math.log(n))
print('sine:',math.sin(n))