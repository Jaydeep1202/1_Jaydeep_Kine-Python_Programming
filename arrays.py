import array as arr
a= arr.array('i',[1,2,3])
print("Integer Array is: ")
for i in range (0,3):
    print(a[i],end=" ")
print("\n")

b=arr.array('d',[1.2,3.2,5.6,7.4])
print("Float Array is: ")
for j in range(0,len(b)):
    print(b[j])

#add element
a.insert(0,4)           #at index 0, element 4
print(a)

a.append(5)             #add element at start
print(a)

#remove element
a.remove(2)             #remove element 2
print(a)

a.pop()
print(a)                #remove last element

#print array
for i in a:
    print(i)
print("\n")
print(a[2])
