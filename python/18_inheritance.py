'''
# W3schools Notes

# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Create a Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class:

# Create a class named Person, with firstname and lastname properties, and a printname method:
'''
class Person:
  def __init__(self, fname, lname):     #Note: The __init__() function is called automatically every time the class is being used to create a new object. Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
    self.firstname = fname
    self.lastname = lname

  def printname(self):
   print("Welcome", self.firstname, self.lastname, "to the class of",self.graduationyear) #Add a method called welcome to the Student class:   

class Student(Person): #Create a Child Class # To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
  def __init__(self, fname, lname,year):
    super().__init__(fname,lname)       # Python also has a super() function that will make the child class inherit all the methods and properties from its parent:  By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
    self.graduationyear = year          #the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function: Add a year parameter, and pass the correct year when creating objects:
  # pass                 #Note: Use the pass keyword when you do not want to add any other properties or methods to the class.


x = Student("John", "Doe",2019)     #Use the Person class to create an object, and then execute the printname method:
x.printname()

x = Student("Mike", "Olsen",2022)       #Now the Student class has the same properties and methods as the Person class.Use the Student class to create an object, and then execute the printname method:
x.printname()


'''
# Harry notes
# There are three types of inheritance single,multiple,multilevel inheritance
'''
# Single Inheritance

class Employee:
    company = "Google"
    
    def showDetails(self):
        print("This is an employee")
class programmar(Employee):
    language="Python"
    company="Youtube"

    def getLanguage(self):
        print(f"The Language is {self.language} and work in {self.company}")

    def showDetails(self):
        print("This is an programmar")

e = Employee()
e.showDetails()
p= programmar()
p.showDetails()
p.getLanguage()
print(p.company)

# Multiple Inheritance

class Freelancer:
    company="Fiver"
    level=0
    def upgradeLevel(self):
        self.level = self.level + 1
        print(self.level)

class Employees:
    company ="Visa"
    eCode=120

class programmars(Freelancer,Employees):    #the output show result first company which one class input first
    name ="Rohit"

q = programmars()
q.upgradeLevel()
q.upgradeLevel()
print(q.company)

# MultiLevel Inheritance

class Person:
    country = "India"
    def takeBreath(self):
        print("I am breathing....")
class Employer (Person):
    company= "Honda"
    def getSalary(self,salary):
        self.salary=salary
        print(f"Salary is {self.salary}")
    def takeBreath(self):
        print("I am an Employee so i am luckily breathing")
class program(Employer):
    company="Fiver"
    def getSalary(self):
        print("No salary to programmers")
    def takeBreath(self):
        print("I am a programmer ao i am breathing++...")

r = Person()
r.takeBreath()
print(r.country)

s=Employer()
s.getSalary(1200)
s.takeBreath()
print(s.company)

t = program()
t.takeBreath()
print(t.company)
print(t.country)
t.getSalary()

# Super class
class People:
    countries="Japan"
    def __init__(self):
        print("Intializing Person...\n")
    def takeBreath(self):
        print("I am breathing....")
class Worker(People):
    company="Suzuki"
    def __init__(self):
        super().__init__()
        print("Initializing Employee...\n")
    def getSalary(self):
        print(f"Salary is {self.salary}")
    def takeBreath(self):
      super().takeBreath()
      print(f"I am Employee so I am luckily breathing....")
class Engineer(Worker):
    company="Google"
    def __init__(self):
        # super().__init__()
        print("Intializing Programmar...\n")
    def getSalary(self):
        print(f"No salary to programmars")
    def takeBreath(self):
        super().takeBreath()
        print("I am a programmar so I am breathing++....")

u = People()
u.takeBreath()

v = Worker()
v.takeBreath()

w = Engineer()
w.getSalary()
w.takeBreath()

# Class Method
class Employers:
    company="Camel"
    salary=100
    location = "delhi"

    # def changeSalary(self,sal):
    #     self.__class__.salary=sal

    @classmethod
    def changeSalary(cls,sal):
        cls.salary=sal


x = Employers()
print(x.salary)
x.changeSalary(465)
print(x.salary)
print(Employers.salary)

# Property Decorator

class Labour:
  company="Bharat Gas"
  salary = 5600
  salaryBonus=400

  @property
  def totalSalary(self):
    return self.salary + self.salaryBonus
  
  @totalSalary.setter
  def totalSalary(self,val):
    self.salaryBonus=val-self.salary

y = Labour()
print(y.totalSalary)
y.totalSalary=5000
print(y.salary)
print(y.salaryBonus)

# Operator Overloading 
class Number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2):
        print("Let's add")
        return self.num + num2.num
    def __mul__(self,num2):
        print("Lets multiply")
        return self.num * num2.num
    def __str__(self):
        return f"Decimal Number: {self.num}"
    def __len__(self):
        return len(str(self.num))
n1 = Number(2)
n2 = Number(4)
sum = n1 + n2
mul = n1 * n2
print(sum)
print(mul)
n = Number(11)
print(n)
print(len(n))
