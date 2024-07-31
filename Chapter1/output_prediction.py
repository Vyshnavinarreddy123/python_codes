#output prediction

count=0
while count<10:
    print("hi")
    count+=1


x=10
y=0
while x>y:
    print(x,y)
    x=x-1
    y=y+1


keep=True
x=100
while keep:
    print(x)
    x=x-10
    if x<50:
        keep=False
'''
x=45
while x<50:
    print(x)'''

for x in [1,2,3,4,5]:
    print(x)

for i in range(1,10):
    print(i)


for z in range(-500,500,100):
    print(z)


x,y=10,5
for i in range(x-y*2):
    print("%",i)

c=0
for x in range(10):
    for y in range(5):
        c+=1
print(c)


x='one'
y='two'
counter=0
while counter<len(x):
    print(x[counter],y[counter])
    counter+=1
