#int
a=1        
print(a)

#string
b="jaydeep"
print(b)

#list
c=[1,"jd",89.00]
print(c)
c[0]=2
print(c)

#tuple
e=(1,"ad",99.00)
print(e)

#range
f=range(4,21,5)
for n in f:
    print(n)

#bool
g=True
print(g)

#mapping / dictionary                      subdictionary
dict1 = {1:"jay",2:'ath',3:"sid",'a':"har",4:{5:"vj",b:"uttu"}}
print(dict1)
print(dict1.keys())
print(dict1.values())


#typeof
print(type(a))

#sizeof
print(len(b))

#set
set1=set([1,2,3,3])
print(set1)
set1.add(4)
print(set1)

#frozenset
set2=frozenset([11,"cat"])
print(set2)

#check elements in set
print(1 in set1)
print("cat" in set2)
print("ath" in set2)

#binary byte
str1 = "jd"
arr1=bytes(str1,'utf-8')
print(arr1)

#binary bytearray
str2="hello"
arr2=bytearray(str2,'utf-8')
print(arr2)

#memoryview
b_arr=bytearray('jd','utf-8')
mv=memoryview(b_arr)
print(mv[0])
