# print prime numbers in between 1 and user input
import math
def prime(n):
    if n<2:
        return False
    elif n==2:
        return True
        i=3
        while(i<=math.sqrt(n)):
        if n%i==0:
            return False
        return True
n= int(input())
for num in range(2,n+1):
    if prime(num):
        print(num, end=" ")