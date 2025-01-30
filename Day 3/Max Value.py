def display(data):
    print(f"The max val is: {data}")

def get_input():
    x= input("Enter 1st num:")
    y= input("Enter 2nd num")
    z= input("Enter 3rd num:")
    return (x,y,z)

def max(x,y,z):
    if(x>y and x>z):
        return x
    if(y>x and y>z):
        return y
    if(z>x and z>y):
        return z
    
def main():
    (x,y,z)=get_input()
    res= max(x,y,z)
    display(res)
main()