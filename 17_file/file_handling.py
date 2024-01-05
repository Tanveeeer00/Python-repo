# W3schools codes and notes
'''
Python has several functions for creating, reading, updating, and deleting files.

File Handling
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)

Syntax
To open a file for reading it is enough to specify the name of the file:

f = open("17_file/demofile.txt")
The code above is the same as:
f = open("17_file/demofile.txt", "rt")

Because "r" for read, and "t" for text are the default values, you do not need to specify them.
Note: Make sure the file exists, or else you will get an error.
'''

# file open
# To open the file, use the built-in open() function.
# The open() function returns a file object, which has a read() method for reading the content of the file:

# we have the following file, located in the same folder as Python:
a=open("01_hello.py","r")
print(a.read())

# If the file is located in a different location, you will have to specify the file path, like this:
b=open("17_file/demofile.txt","r")
print(b.read())

# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
c=open("17_file/demofile.txt","r")
print(c.read(12))

# Read Lines
# You can return one line by using the readline() method:
d=open("17_file/demofile.txt","r")
print(d.readline())
# by default r
e=open("17_file/demofile.txt")
print(e.readline())

# loop in line
# By looping through the lines of the file, you can read the whole file, line by line:
f=open("17_file/demofile.txt","r")
for loo in f:
    print(loo)

# close files
# It is a good practice to always close the file when you are done with it.
g=open("17_file/demofile.txt","r")
print(g.readline())
g.close()
# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.

# file write
'''
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
'''

# appending 
# create file and add content if file does not exist
h=open("17_file/demofile2.txt","a")
h.write("hello world\n now the file has more content ")
h.close()
h=open("17_file/demofile2.txt","r")  #open and read the file after the appending:
print(h.read())

# add content to the end of the file if file exist
j=open("17_file/sample.txt","a")
j.write("\nhello world\ncreate demofile2.txt\n now the file has more content ")
j.close()
j=open("17_file/sample.txt","r")  #open and read the file after the appending:
print(j.read())


# write
# create file and add content if file does not exist

k = open("17_file/demofile3.txt","w")
k.write("Woops! i have deleted the content!")
k.close()
k=open("17_file/demofile.txt","r")
print(k.read())

# Open the file "demofile3.txt" and overwrite the content:
# Note: the "w" method will overwrite the entire file.
l=open("17_file/demofile3.txt","w")
l.write("previous one deleted")
l.close()
l=open("17_file/demofile3.txt","r")   #open and read the file after the overwriting:
print(l.read())


# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exist
# Result: a new empty file is created!
i=open("17_file/demofile4.txt","x")

# "w" - Write - will create a file if the specified file does not exist
# Create a new file if it does not exist:
m = open("17_file/demofile5.txt", "w")

# "a" - Append - will create a file if the specified file does not exist
# Create a new file if it does not exist:
n=open("17_file/demofile6.txt","a")


# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:
import os
os.remove("17_file/demofile6.txt")


# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:
import os
if os.path.exists("17_file/demofile5.txt"):
    os.remove("17_file/demofile5.txt")
else:
    print("The file does not exist")


# Delete Folder
# To delete an entire folder, use the os.rmdir() method:
# Note: You can only remove empty folders.
import os
os.rmdir("17_file/samplef")





# harry code

# Use open function to read the content of a file!
o = open('17_file/sample.txt','r') 
o = open('17_file/sample.txt') # by default the mode is r
# data=o.read()
data=o.read(10) # reads first 5 characters from the file
print(data)
# print(o.read())  #alternative to print
o.close()

# readline
p = open("17_file/sample.txt")
# Read first line
datan=p.readline()
print(datan)
# Read second line
datan=p.readline()
print(datan)
# Read third line
datan=p.readline()
print(datan)
# Read fourth line
datan=p.readline()
print(datan)
p.close()

# write
q=open("17_file/another.txt","w")
q.write("hello \n this is another file")
q.write("world \n this is another line")

q.close()

#with
# the best way to open and close the file automatically is the with statement
with open("17_file/another.txt","r") as r:
    s = r.read()
with open("17_file/another.txt","w") as r:
    s = r.write("me")
print(s)



