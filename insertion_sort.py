l=[]

n=int(input("Enter Total Number of Elements"))

for i in range(0,n):
    l.append(int(input()))

print("Before Sorting : ",l)

for i in range(1,n):  
    j=i-1
    temp=l[i]
    while j>=0 and temp<l[j]:
        l[j+1]=l[j]
        j=j-1
    l[j+1]=temp

print("After Sorting : ",l)
        
