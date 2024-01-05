
# Write a program to read the text from a given file "poem.txt" and find out whether it contains the word "twinkle".
# b=open("17_file/poem.txt","w")
# b.write("Twinkle little star!\n How i wonder what are you")
# print(b.write())

a = open("17_file/poem.txt")
c=a.read()
if "Twinkle" in c:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
a.close()

# The game() function in a program lets a user play a game and returns the score as an integer.You need to read a file "hiscore.txt" which is either blank or contains the previous hi-score you need tyo write a program to update the hi-score whenever game() breaks the hi-score 
def game():
    return 4550
score=game()
with open("17_file/hiscore.txt") as f:
    hiscorestr= f.read()
if hiscorestr=="":
    with open("17_file/hiscore.txt","w") as f:
        f.write(str(score))
elif int(hiscorestr)<score:
    with open("17_file/hiscore.txt","w") as f:
        f.write(str(score))

# Write a program to generate multiplication tables from 2 to 20 and write it to the different file.place these files in a folder for a 13 year old.
for i in range(2,21):
    with open(f"17_file/tables/Multiplication_of_table_{i}.txt","w") as g:
        for j in range(1,11):
            g.write(f"{i}X{j}={i*j}")
            if j!=10:
                g.write("\n")

# A file contains a word "donkey" multiple times. you need to write a program which replaces this word with ###### by updating the sane file.
with open("17_file/update.txt","w") as l:
    for k in range(32):
        l.write("donkey\n")

with open("17_file/update.txt") as l:
    contents = l.read()
contents=contents.replace("donkey","#$&%*#")
with open("17_file/update.txt","w") as l:
    l.write(contents)
    
# # Repeat program 4 for a list of such words to be censored
words=["donkey","kaddu","motu"]
with open("17_file/update.txt") as m:
    content=m.read()
for word in words:
    content=content.replace(word,"#$&%*#")
    with open("17_file/update.txt","w") as m:
        m.write(content)

# Write a program to mine a log file and find out whether it contains "python"
with open("17_file/log.txt") as n:
    cont=n.read()
if "PYTHON" in cont.upper():
    print("Yes python is present")
else:
    print("No python word is present")

# Write a program to find out the line number where python is present from question 6
conte=True
i = 1
with open("17_file/log.txt") as o:
    while conte:
        conte=o.readline()
        if "PYTHON" in conte.upper():
            print(conte)
            print(f"Yes python is present in line no {i}")
        i+=1

# Write a program to make a copy of a text file "this.txt"
with open("17_file/copy.txt","r") as p:
    conten=p.read()
with open("17_file/copied.txt","w") as p:
    p.write(conten)

# Write a program to find out whether a file is identical & matches the content of another file

# file1=("17_file/copy.txt")
# file2=("17_file/copied.txt")
# with open("17_file/copied.txt","r") as q:
#     f1=q.read()
# with open("17_file/copy.txt","r") as r:
#     f2=r.read()
#     if f1==f2:
#         print("yes this file is identical")
#     else:
#         print("this file is not identical")

file1="17_file/copy.txt"
file2="17_file/copied.txt"
with open(file1) as q:
    f1= q.read()
with open(file2) as r:
    f2= r.read()
    if f1==f2:
        print("yes this file is identical")
    else:
        print("this file is not identical")

# Write a program to wipe out the contains of a sfile using python

with open("17_file/wipe.txt","w") as s:
    s.write("")
    
# # write a python program to rename a file to "renamed_by_python.txt"

# import os
# with open("17_file/rename.txt") as t:
#     contents=t.read()
# with open("17_file/renamed_by_python.txt","w") as t:
#     t.write(contents)
# os.remove("17_file/rename.txt")

import os
oldname="17_file/rename.txt"
newname="17_file/renamed_by_python.txt"
with open(oldname) as t:
    contents=t.read()
with open(newname,"w") as t:
    t.write(contents)
os.remove("oldname")
