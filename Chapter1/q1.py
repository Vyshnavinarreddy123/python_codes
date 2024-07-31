#write a program to print cubes of numbers in the range 15 to 20

for i in range(15,21):
    print("cube of",i,"is=",end="")
    print(i**3)
print()


#write a program to print square root of every alternate number in the range 1 to 10

for element in range(1,11):
    print("square root of ",element,"is=",end="")
    print(element ** 0.5)
print()

#write a program that multiple two integer num with out using * operator ,using repeated addition

n1=(int(input("enter n1")))  #4
n2=int(input("enter n2"))       #2
count=n1                 #count=4              
product=0
while count>0:
    product+=n2
    count-=1
print("product of ",n1,"and ",n2,"is=",product)
    
    
