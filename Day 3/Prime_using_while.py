# User input should be determined whether prime or not using while loop
import math
def prime(n):
    if n==2:
        return "Prime"
    elif n%2==0:
        return "Not Prime"
    i=3
    while(i<=math.sqrt(n)):
        if(n%i==0):
            return "Not Prime"
        i+=2
    return "Prime"
    
def main():
    n=int(input())
    val= prime(n)
    print(val)
main()
