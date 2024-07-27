import math as m
for i in range(1,5):
    for j in range(1,8):
        mid=(1+j)/2
        mid=m.ceil(mid)
        
        for k in range(1,mid+1):
            if k!=mid:
                print(i,end="")
            else:
                print(" ",end="")
    print()
