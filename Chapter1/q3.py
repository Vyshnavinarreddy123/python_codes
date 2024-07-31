#write a program that reeatedly asks from users some numbers until string is 'done' is typed. The program should print the sum of all numbers entered

n=input("enter string")
sum=0
while n!='done':
    n=int(n)
    sum+=n
    n=input("enter string")
print(sum)
