
#printing prime numbers

num=int(input("enter value"))

for i in range(2,num):
    if num%i==0:
        print( "non prime")
        break
    else:
        print("prime")
        break
        
