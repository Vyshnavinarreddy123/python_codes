import math as m
n=int(input("enter n"))
x=int(input("enter x"))
z=1
for i in range(1,n+1):
    z=2*z*i
print("fact",z)
    
def cosfunction_1(n):
    y=m.pow(x,2*n)
    z=y/z
    x=x*z*(m.pow(-1,n))
print(x)

    
    
