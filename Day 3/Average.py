# Define a function to dsiplay the parameter
def display(data):
    print(f"The average is: {data}")

# Takes the imput from user
def get_input():
    a=input("Enter 1st num:")
    b=input("Enter 2nd num:")
    c=input("Enter 3rd num:")
    d=input("Enter 4th num:")
    n=input("Enter the avg num:")
    return(a,b,c,d,n) 

# Computes the sum of 4 numbers
def sum(a,b,c,d):
    sum1= (int(a)+int(b)+int(c)+int(d))
    return (sum1)

# Computes the average of the sum1 value
def average(sum1,n):
    avg=int(sum1)/int(n)
    return (avg)

# Calls the above functions
def main():
    (a,b,c,d,n)= get_input()
    comp_sum= sum(a,b,c,d)
    comp_avg= average(comp_sum,n)
    display(comp_avg)
main()