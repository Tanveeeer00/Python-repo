

'''
PascalCase 
EmployeeName -->PascalCase 

camelCase
isNumeric, isFloatOrInt -->camelCase
'''

'''
Python Classes/Objects
Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.A Class is like an object constructor, or a "blueprint" for creating objects.
'''

# To create a class, use the keyword class:
class number:
    def sum(self):
        return self.a + self.b

num = number()
num.a = 65
num.b = 45
s = num.sum() 
print("The sum of a and b is",s)

import pandas as pd
pd.DataFrame()
class RailwayForm:
    formType="Railwayform"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
tanapplication=RailwayForm()
tanapplication.name = "Tanveer"
tanapplication.train ="Rajdhani"
tanapplication.printData()

class Employee:
    company="youtube"
    salary=100
    incentives=200
harry= Employee()
tanveer=Employee()
harry.salary=200
tanveer.salary=300
# Creating instance attributes incentives for both the objects
tanveer.incentives=100
print(tanveer.incentives)
print(harry.incentives)

print(harry.company)
print(tanveer.company)
Employee.company="Google"
print(harry.company)
print(tanveer.company)
print(harry.salary)
print(tanveer.salary)

# Below line throws an error as address is not present in instance/class 
# print(harry.address) 


class Employees:
    companies = "Chrome"
    def getSalary(self,signature):
        print(f"Salary for this employee working in {self.companies} is {self.salaries}\n{signature}")
    @staticmethod
    def greet():
        print("Good Morning sir")
    @staticmethod
    def time():
        print("The time is 9am in the morning")
kaif=Employees()
kaif.salaries=100000
# kaif.getSalary() #Employees.getSalary(kaif)
kaif.getSalary("Thanks!") #Employees.getSalary(kaif)
kaif.greet() #Employees.greet()
kaif.time()



'''
The __init__() Function
To understand the meaning of classes we have to understand the built-in __init__() function.All classes have a function called __init__(), which is always executed when the class is being initiated.Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
Note: The __init__() function is called automatically every time the class is being used to create a new object.
'''

class worker:
    firm = "linux"
    def __init__(self,naam,wages,subunit):
        self.naam=naam
        self.wages=wages
        self.subunit=subunit
        print("Employee is created")
    def getDetails(self):
        print(f"The name of the employee is {self.naam}")
        print(f"The name of the employee is {self.wages}")
        print(f"The name of the employee is {self.subunit}")
    def getWages(self,signture):
        print(f"Salary for this employee working in {self.firm} is {self.wages}\n{signture}")
    @staticmethod
    def gret():
        print("Good morning,sir")
    @staticmethod
    def clock():
        print("The time is 9am in the morniing")
nida=worker("Nida",10000,"linux")
nida.getDetails()
nida.gret()
nida.clock()
nida.firm="youtube"
nida.getWages("Thanks")
#nida = worker() #--> This throws an error (missing 3 required positional arguments:)

'''
The __str__() Function
The __str__() function controls what should be returned when the class object is represented as a string.If the __str__() function is not set, the string representation of the object is returned:
'''

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}({self.age})"
p1 = person("john",36)
print(p1)


'''
Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.
'''

class Persons:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p2 = Persons("John", 36)
p2.myfunc()

'''
The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

Modify Object Properties
You can modify properties on objects like this:
p1.age = 40

Delete Object Properties
You can delete properties on objects by using the del keyword:
Delete the age property from the p1 object:

# del p1.age


Delete Objects
You can delete objects by using the del keyword:
Delete the p1 object:

# del p1


The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Person:
  pass
  
'''