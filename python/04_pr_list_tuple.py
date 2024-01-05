# Write a program to store seven fruits in a list entered by the user 
f1=input("Enter Fruit Name 1: ")
f2=input("Enter Fruit Name 2: ")
f3=input("Enter Fruit Name 3: ")
f4=input("Enter Fruit Name 4: ")
f5=input("Enter Fruit Name 5: ")
f6=input("Enter Fruit Name 6: ")
f7=input("Enter Fruit Name 7: ")
myFriutLiat=[f1,f2,f3,f4,f5,f6,f7]
print(myFriutLiat)

# Write a program to accept marks of 6 students and display then in a sorted manner
m1=int(input("Enter marks of students 1: "))
m2=int(input("Enter marks of students 2: "))
m3=int(input("Enter marks of students 3: "))
m4=int(input("Enter marks of students 4: "))
m5=int(input("Enter marks of students 5: "))
m6=int(input("Enter marks of students 6: "))
myList=[m1,m2,m3,m4,m5,m6]
myList.sort()
print(myList)


# Check that a tuple cannot be changed in python 
ch_list=("5","6","9")
# ch_list[1]="10"       #tuple cannot be changed in tuple

# another way to change
x=list(ch_list)
x[1]= "10"
ch_list=tuple(x)
print(ch_list)

# Write a program to sum a list with 4 numbers.
a=[1,2,3,4]
print(a[0]+a[1]+a[2]+a[3])
# Another way to add
print(sum(a))

# Write a program to count the number of zeros in the following tuple:
t=(7,0,8,0,0,9)
print(t.count(0))
