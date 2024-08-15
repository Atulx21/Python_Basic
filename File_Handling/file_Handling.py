"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

"""


f=open("text.txt","r")
print(f.read())


#print(f.readline()) 

#f=open("text.txt","a")
#f.write("I failed more than you tried ....\n")

f.close()

f=open("created.txt","x")
f=open("created.txt","a")
f.write("I created This file...")

#To delete file
"""
import os
if os.path.exists("created.txt"):
    os.remove("created.txt")

"""
#to delete folder use 
    #  os.rmdir("Folder name")




