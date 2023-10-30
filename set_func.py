s={'a','b','c','d'}
print(s)

#add element
s.add('e')
print(s)

#deleting element
s.discard('b')
print(s)
s.remove('c')
print(s)
s.pop()             #deletes random element
print(s)
s.clear()           #removes all elements
print(s)

s1={1,2,3}
s2={2,3,4}

print(s1.intersection(s2))
print(s1.union(s2))
print(s1.symmetric_difference(s2))

s1.update(s2)
print(s1)

s1.update("JD")
print(s1)

#convert list to set
l1=[1,2,3,4]
s3=set(l1)
print(s3)
