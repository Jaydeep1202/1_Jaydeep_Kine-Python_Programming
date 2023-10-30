t1=(1,2,3,4,2)
print(t1)
print(t1[2])

#repetetion
t2=t1*2;
print(t2)

#count
count = t1.count(2)
print("Number of times 2 is in t1: ",count)

#print at what index is 4 present
i=t1.index(4)
print("4 is present at index: ",i)

#delete tuple
del t1
