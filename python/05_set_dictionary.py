
# write a program to create a dictionary of hindi words with values as their english translation provide user with an option to look it up!

mydict={
"Pankha":"fan",
"Dabba":"Box",
"Vastu":"item"
 }
print("option are ",mydict.keys())
a=input("Enter the Hindi Word\n")
# print("The meaning of your word is:",mydict[a])
# below line will not throw an error if the key is not present in the dictionary
print("The meaning of your word is: ",mydict.get(a))


# Write a program to input eight numbers ffrom the user and display all the unique numbers(once)

num1 = int(input("Enter the number 1\n "))
num2 = int(input("Enter the number 2\n "))
num3 = int(input("Enter the number 3\n "))
num4 = int(input("Enter the number 4\n "))
num5 = int(input("Enter the number 5\n "))
num6 = int(input("Enter the number 6\n "))
num7 = int(input("Enter the number 7\n "))
num8 = int(input("Enter the number 8\n "))
s={num1,num2,num3,num4,num5,num6,num7,num8}
print(s)

# Can we have a set with 18(int) and "18"(str) as a values in it?
b={18,"18",18.1}
print(b)

# What will be the length of following set s and its type
c={20,"20",20.0}
print(c)
print(len(c))
print(type(c))

# Create an empty dictionary allow 4 friends to enter their favorite language as values and use keys as their names.Assume that the names are unique
favlang={}
a= input("Enter your favorite language Shubham:\n")
b= input("Enter your favorite language Ankita:\n")
c= input("Enter your favorite language Sonali:\n")
d= input("Enter your favorite language Harsita:\n")
favlang["Shubham"] = a
favlang["Ankita"] = b
favlang["Sonali"] = c
favlang["Harshita"] = d
print(favlang)
