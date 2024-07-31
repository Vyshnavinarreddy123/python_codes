#Write a python program that return True if num is even else false
def odd_even(n):
    if n%2==0:
        t1=True
    else:
        t1=False
    return t1
n=int(input("enter a number"))
print(odd_even(n))
