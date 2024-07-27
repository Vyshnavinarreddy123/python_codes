print("break statement")
for i in range(10):
    if i==1:
         print("i is 1")
         break
    else:
         print("i is not 1")

print()
print("continue statment")
for j in range(10):
    if j%4==0:
        print(j," divided by 4")
        continue
    else:
        print(j,"is not divided by 4")
        
print()
for j in range(1,21):
    if j%3==0 or j%5==0:
       continue
    else:
        print(j,"not divisible by either 3 or 5")
print("bye")

print()
for j in range(1,10):
    if j<5:
      continue
    else:
        print(j)
