
# Write a program to print multiplication table of a given number using for loop
a = int(input("Enter the number: "))
for b in range(1,11):
    # print(str(a) + " X " + str(b) + " = " + str(a*b))
    print(f"{a} X {b} = {a*b}")

# Write a program to greet all the person names sorted in aa list li and which starts with s
li = ["harry","sohan","sachin","rahul"]
for name in li:
    if name.startswith("s"):
        print(" Hello " + name)

# just for fun practice
nam = input("Enter your name: ")
if nam.startswith("s"):
        print(" Hello " + nam)
else:
    print("This name not start with s")

#  Attempt multiplication table with using while loop
num = int(input("Enter your number: "))
c = 0
while c < 11:
    print(str(num) + " X " + str(c) + "=" + str(num*c))
    c += 1

# Write a program to find whether a given number is prime or not
d = int(input("Enter your number: "))
prime = True
for e in range(2,d):
     if (d%e == 0):
         prime = False
         break
if prime:
   print("This is prime number")
else:
      print("This is not prime number")
  
# write a program to find the sum of first a natural using while loop
f = int(input("Enter your number: "))
factorial = 1
for g in range(1 , f+1):
     factorial *= g
print(f"The factorial of {f} is {factorial}")

#Write a program to find write d the sum of first n natural numbers using while loop in python
# Sum of natural numbers up to num

h = int(input("enter a number: "))

if h < 0:
   print("Enter a positive number")
else:
   i = 0
   # use while loop to iterate until zero
   while(h > 0):
       i += h
       h -= 1
   print("The sum is", i)

# write a program to print star pattern in python
j = 3
for k in range(3):
    print("*"*(k+1))

l = 4
for m in range(4):
    print(" " * (l-m-1),end=" ")
    print("*" * (2*m+1),end=" ")
    print(" " * (l-m-1))

# write a program to print multiplication table of n using for loop in reversed order.
num = int(input("Enter the number: "))
for n in range(10,0,-1):
    print(f"{num} X {n} = {num*n}")