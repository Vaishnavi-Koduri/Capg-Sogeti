import dis
def multiply():
    n=5
    for i in range(n):
        mul=n*i
    return (mul)

def main():
    res= multiply()
    print(res)
    dis.dis(multiply)
main()
