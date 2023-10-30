#int input
num = int(input("Enter number "))
print(num)

#string input
name = input("Enter name ")
print(name)

#map
a,b,c = map(int,input("Enter 3 numbers ").split())
print(a,b,c)

#input in list
l=list()
a=int(input("Enter list size"))
print("Enter elements")
for i in range(0,a):
    l.append(int(input()))
print(l)
