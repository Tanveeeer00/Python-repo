
# A spam comment is defined as a text containing following keyword:
# "make a lot of money","buy now","subscribe this","click this".Write a program to detect these spams.

text = input("Enter the text\n")
if("make a lot of money" in text):
  spam=True
elif("buy now" in text):
  spam=True
elif("subscribe this" in text):
   spam=True
elif("click this" in text):
    spam=True
else:
    spam=False
if(spam):
    print("This is spam")
else:
    print("This is not spam")
    
# Write a program to find greatest of four numbers entered by the user.

num1 = int(input("Enter the number:\n"))
num2 = int(input("Enter the number:\n"))
num3 = int(input("Enter the number:\n"))
num4 = int(input("Enter the number:\n"))
if(num1>num2):
    fi=num1
else:
    f1=num2
if(num3>num4):
    f2=num3
else:
    f2=num4
if(f1>f2):
    print(str(f1)+" is greatest")
else:
    print(str(f2)+" is greatest")
    
# Write a program to find out whether a student is pass or fail,if it requires total 40% and at least 33%,in each subject  to pass.Assume 3 subject and take marks as an input from the user

sum1 = int(input("Enter your English marks\n"))
sum2 = int(input("Enter your maths marks\n"))
sum3 = int(input("Enter your science marks\n"))
# if(sum1<33 or sum2<33 or sum3<33):
    # print("You are fail because you have less than 33% in one of the subjects")
if(sum1<33):
    print("You are fail because you have",sum1," less than 33% in English subject")
elif(sum2<33):
    print("You are fail because you have",sum2," less than 33% in Maths subject")
elif(sum3<33):
    print("You are fail because you have",sum3," less than 33% in Science subject")
elif(sum1 + sum2 + sum3)/300*100<40:
    print("You are fail due to total percentage less than 40")
else:
    print("Congratulation! You passed the exam")

# Write a program which to find whether a given username contains less than 10 containers or not.

name = input("Enter your name:\n")
name1 = len(name)
# print(name1)
if(name1<10):
    print("The username contain less than 10")
elif(name1==10):
    print("The username contain equal to 10")
else:
    print("The username contain more than 10")
    
# Write a program which find out whether a given name is present in a list or not.


a = ["tanveer","kaif","harry","bond"]
b = input("Enter your name:\n")
if b in a:
    print("Yes,Its present in a list of name")
else:
    print("NO,Its not present in a given list")

# Write a program to calculate the grade of a student from his marks from the bfollowing scheme

grades = int(input("Enter your marks: \n"))
if(grades>=90):
    grade = "Ex"
elif(grades>=80):
    grade="A"
elif(grades>=70):
    grade="B"
elif(grades>=60):
    grade="C"
elif(grades>=50):
    grade="D"
else:
    grade="F"
print("Your marks is",grades,"and your grade is "+ grade)


# Write a program to find out whether a given post is talking about "Harry" or not.

post="HaRRy went to the park for a walk."
case_insensitive_post=post.casefold()

if "harry" in case_insensitive_post:
    print("yes, this post is talking about Harry")
else:
    print("no, this post is not talking about Harry")