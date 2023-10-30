import operator as op

#Arithmetic Operators
a=15
b=10
print("Addition is")
print(op.add(a,b))                  #or a+b
print("Multiplication is ")
print(a*b)                          #or op.mul(a,b)
print("Modulus is ")
print(op.mod(a,b))                  #or a%b
print("Power is ")
print(op.pow(a,b))                  #or a**b
print("Floor div is ")
print(op.floordiv(a,b))             #or a//b
print("\n")

#Comparison Operators
x=15
y=5
print("Greater than")
print(x>y)                          #or gt(x,y)
print("Greater than equal to")
print(op.gt(x,y))                   #or x>=y
print("Not equal to")
print(op.ne(x,y))                   #or x!=y
print("\n")

#Logical Operators
p=1
q=0
print("AND")
print(p and q)
print("OR")
print(p or q)
print("NOT")
print(not q)
print("\n")

#Bitwise Operators
c=0
d=1
e=20
print("Invert")
print(op.invert(d))                 #or ~d
print("XOR")
print(c^d)                          #or op.xor(c,d)
print("Right shift")
print(e>>2)
print("\n")

#Assignment Operators
v=10
w=15
print("Plus equal")
v+=w
print(v)
print("Mul equal")
v*=w
print(v)
print("\n")

#Membership Operators
x=24
y=30
l=[10,20,30,40]
print("Is 24 in list")
print(x in l)
print("Is 30 in list")
print(y in l)
print("\n")

#Identity Operators
a=10
b=20
c=a
print("a is not b")
print(a is not b)
print("a is c")
print(a is c)
print("\n")
