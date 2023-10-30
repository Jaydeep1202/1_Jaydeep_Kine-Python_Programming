import os

#create new directory/folder
os.mkdir('C:/Jaydeep Python Pracs/JD')

#get current work directory
print("String Format: ",os.getcwd())
print("Byte Format: ",os.getcwdb())

#rename a file in cwd
os.rename('hello.txt','hello2.txt')

#rename and move to other directory
os.renames('hello2.txt','C:/test file/hello3.txt')

#change current directory
print("Current Directory: ",os.getcwd())
os.chdir('C:/test file')
print("Current Directory: ",os.getcwd())

#get size of directory
print(os.path.getsize('C:/Jaydeep Python Pracs'))

#display list of files
print("Files in current directory: ",os.listdir(os.getcwd()))
print("Directory contents are: ",os.listdir('C:/Jaydeep Python Pracs'))

#to remove directory

dir_list=os.listdir('C:/delete file')
if len(dir_list)==0:
    print("Directory is empty")
os.rmdir('C:/delete file')

#to check directory
print(os.path.isdir('C:/test file'))
   
#last accessed and modified time
print("Last accessed time: ",os.path.get.atime('D:/test'))
print("Last modified date: ",os.path.get.mtime('D:/test'))
