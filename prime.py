l= []

n=int(input("Enter Total Number of Elements"))

for i in range(0,n):
    l.append(int(input("Enter elements")))

prime=[]

for i in l:
    count=0
    for j in range(1,i+1):
        if i%j == 0:
            count=count+1

    if count==2:
        prime.append(i)

print(prime)

