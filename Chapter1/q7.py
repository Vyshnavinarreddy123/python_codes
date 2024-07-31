#write a python program that accepts two integers from the user and prints a message saying if first number is divisible by second number or if it is not

n1=int(input("enter n1"))
n2=int(input("enter n2"))

if(n1%n2==0):
    print(n1,"is divisible by",n2)
else:
    print(n1,"is not divisible by",n2)
