from array import *
val=array("i",[6,4,7,2,-1])
#buffer_info() helps to predict size 
print(val.buffer_info())


from array import *
val=array("i",[53,67,3])
#typecode helpss to print type of code you gave
print(val.typecode)

#append ~ adding element at last
val.append(5)
print(val)

#reverse
val.reverse()
print(val)

#printing all number in an array 1st method
for i in range(0,len(val)):
    print(val[i])

#printing all number in an array 2nd method
for i in val:
    print(i)

#copying old array into new array
newArray=array(val.typecode,(a for a in val))
for i in newArray:
    print(i)


