#reading in file using for loop
file = open ("input.txt","r")
for a in file:
    print(a)

#read data in file using function    
file = open ("input.txt","r")
print(file.read())

#read data in file using with statement
with open("input.txt",'r') as file:
    data=file.read()
print(data)

#read certain number oc chars
file = open("input.txt",'r')
print(file.read(5))

#using readline func
file = open("input.txt",'r')
print(file.readline(6))

#using readlines func
file.seek(0)
print(file.readlines())
file.close()

#split func
file=open("input.txt",'r')
data=file.readlines()
for line in data:
    word = line.split()
    print(word)

for line in data:
    word = line.split('*')      #removes *
    print(word)

#write data to file
file=open("output.txt",'w')
word="Jaydeep\n"
line=["Line 1\nLine2\nLine3\n"]
file.write(word)
file.writelines(line)
file.close()
