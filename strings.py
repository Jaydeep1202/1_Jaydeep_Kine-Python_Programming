import string as s

str="Hello"
print(str)
str="""Multi
        Line"""
print(str)

#Accessing charesters in string
str="Jaydeep"
print(str[0])
print(str[-1])
print("\n")

#String reverse
str="Atharva"
print(str[::-1])
print("\n")

#String Slicing
str="Siddhesh"
print(str[1:4])
print("\n")

#String Update
str="Hello"
list1=list(str)
list1[0]='c'
str1=' '.join(list1)
print(str1)
print("\n")

#Delete Charecter
str="DYPCET"
print(str)
str1=str[0:3]+str[4:]
print(str1)
print("\n")

#Delete Entire String
str="College"
print(str)
del str
print(str)
print("\n")

#Formatting
str="{1}{0}{2}".format("Hello","Hi","Welcome")
print(str)
str="{h}{f}{g}".format(f="Hello",g="Hi",h="Welcome")
print(str)

#Allignent
str="{:<20}{:^20}{:>20}".format("Hello","Hi","Welcome")
print(str)

#function
str="Hello"
print("Uppercase",str.upper())
print("Uppercase",str.lower())
