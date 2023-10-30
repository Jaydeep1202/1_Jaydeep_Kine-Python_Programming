d1={1:"Hello",2:"Hi",'a':"Jaydeep"}
print(d1.keys())            #prints keys
print(d1.values())          #prints values
print(d1.items())           #prints key and values
print(d1)
print(d1.get('a'))          #prints value at key:a
newd=d1.copy()              #copy to new dictionary
print(newd)

#delete specific element
print("Deleted elements is: ",d1.pop(2))
print(d1)

#delete last element
print("Deleted element is: ",d1.popitem())
print(d1)

#add elements by combining dictionary
d2={4:"JD"}
d1.update(d2)
print(d1)

#set to dictionary with common value: 1
d3={'a','b','c'}                    #keys
d4=dict.fromkeys(d3,1)
print(d4)

