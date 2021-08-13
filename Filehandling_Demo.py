"""
Step1: Open File with Read/Write Access
read/Write File
Close file

"""

myFile  = open("Welcome.txt","a")
myFile.write("My Name is Parth and I am a Microsoft certified trainer helping students in Developing Programming skills ")

myFile = open("Welcome.txt",'r')
print(myFile.readlines())