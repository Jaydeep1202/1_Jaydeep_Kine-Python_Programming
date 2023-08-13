list1=[]
list2=[]

n=int(input("Enter size of list: "))
for i in range(0,n):
    list1.append(int(input("Enter elements: ")))

print("Before: ",list1)

for i in list1:
    if i not in list2:
        list2.append(i)
print("After Removing Duplicate values: ",list2)
