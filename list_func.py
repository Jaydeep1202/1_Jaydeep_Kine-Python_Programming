l1 = [1,2,"Hello",3.4]
print(type(l1))

print(l1[0:])
print(l1[:])
print(l1[2:4])
print(l1[:3])
print(l1[1:4:2])
print(l1[-1])
print(l1[-3:-1])

l1[2] = 10
print(l1)
l1[2:4]=[49,76]
print(l1)

#repetition
l2=l1*2;
print(l2)

#concatenation
l3=l1+l2
print(l3)
print(len(l3))

#iteration
for i in l3:
    print(i)

#membership
print(i in l1)

#add elements in list
l4=[]
n=int(input("Enter number of elements in list: "))
for i in range(0,n):
    l4.append(input("Enter elements: "))
for i in l4:
    print(i,end=" ")                        #for spacing

print("\nLenght is: ",len(l4))
print("Min is: ",min(l4))
print("Max is: ",max(l4))

#remove elements
l1.remove(2)
print(l1)
