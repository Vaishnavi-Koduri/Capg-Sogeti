def fib(n):
    if n<0:
        return -1
    if(n==0):
        return 0
    if(n==1):
        return 1
    ans= fib(n-2)+fib(n-1)
    return (ans)

def main():
    n= int(input("Enter the number: "))
    for i in range(n):
        res= fib(i)
        print("The series is: ",res)
main()