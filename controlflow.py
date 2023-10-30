#if statement
a = 100
if a:
    print("In if statement")
    print(a)
print("Outside if")
print("\n")

#if else
b=200
if b<100:
    print(b," is Less than 100")
else:
    print(b," is Greater than 100")
print("\n")

#elif
amount = int(input("Enter Amount "))
if amount>1000:
    discount=amount*0.5
elif amount>500:
    discount=amount*0.2
else:
    discount=amount*0.1
print("Discount is: ",discount)
print("\n")

#else with while
count = 0
while count<5:
    print(count)
    count=count+1
else:
    print(count)
print("\n")

#while
num=0
while num<3:
    num=num+1
    print("Hi")

lis=[1,2,3,4]
while lis:
    print(lis.pop())
print("\n")

#shorthand if
c=20
if c==20:print("Value is 20")
print("\n")

#shorthand if else
d=300
print("value less than 200")if(d<200)else print("value more than 200")
print("\n")

#for
l=["first",1,2.0]
for x in l:
    print(x)
print("\n")

#continue
for n in "dypcet":
    if n=='p' or n=='t':
        continue;
    print("Letter ",n)
print("\n")

#break
for m in "kolhapur":
    if m=='h' or m=='p':
        break;
    print(m)
print("\n")

#pass
for k in "jd123":
    pass
print(k)
print("\n")
