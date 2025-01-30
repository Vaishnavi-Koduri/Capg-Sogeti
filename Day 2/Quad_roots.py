import cmath
a=int(input())
b=int(input())
c=int(input())

def quad_root(a,b,c):
    discriminant= b**2-4*a*c
    root1= -b + cmath.sqrt(discriminant)/2*a 
    root2= -b - cmath.sqrt(discriminant)/2*a
    return root1, root2
print(quad_root(a,b,c))