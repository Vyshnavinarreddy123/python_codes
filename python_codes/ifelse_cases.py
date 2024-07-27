a=int(input("enter num1"))
b=int(input("enter num2"))
if a==b:
    print("a==b")
    print("num1==num2")
else:
    print("num1<num2")
    print("num1>num2")

c=int(input("enter num3"))
if a<b:
    if a<c:
        print("c is greater")
    else:
        print("b is greater")
else:
    if b<c:
        print("b is greater")
    else:
        print("a is greater")
