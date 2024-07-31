#write aprogram that asks the user to input nuber of seconds and then express in the terms of many minutes and seconds it contains
n=int(input("how many times you want to convert "))
for i in range(1,n+1):
    sec_input=int(input("enter seconds"))
    min=int(sec_input/60)
    sec=int(sec_input%60)
    print("given seconds as= ",sec_input," after converting min=",min," with seconds=",sec)
    print()
