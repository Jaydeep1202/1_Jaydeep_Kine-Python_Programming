//main folder has __init__.py , sum.py, sub.py. Outside this folder demopck.py


//demopck.py
from sumsub import sum
from sumsub import sub
res = sum.sum1(10,20)
print(res)
res = sub.sub1(10,5)
print(res)


//sum.py
def sum1(a,b):
    return a+b


//sub.py
def sub1(a,b):
    return a-b

//__init__.py
empty file
