def fun():
    print("Jd")
print("Hello")
fun()

#parameterised func
def add(num1,num2):
    num3=num1+num2
    return num3

n1=int(input("Enter Num 1: "))
n2=int(input("Enter Num 2: "))
sum=add(n1,n2)
print("Sum is: ",sum)

#lambda/anonymous function
c=lambda a:a*a*a
print("Cube is: ",c(5))
