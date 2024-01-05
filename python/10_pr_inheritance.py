'''
# Create a class C2D vector and use it to create anothers class representing a 3-d  vector
class C2dVec:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dVec(C2dVec):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.kcap = k
    
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
    
    
v2d = C2dVec(1, 3)
v3d = C3dVec(1, 9, 7)
print(v2d)
print(v3d)

# Create a class pets from a class animals and futher create class dog from pets Add s method bark to class dog
class Animals:
    animalType="Manmal"
class Pets:
    color="White"
class Dog:
    @staticmethod
    def bark():
        print("Bow Bow!!")
d=Dog()
d.bark()
'''
# Create a class Employee and add salary and increment properties to it.Wrtie a method SalaryAfterIncrement method with a property decorator with a setter which changes the value of increment based on the salary
# salryAfterIncrement = salary*increment
class Employee:
    salary = 1000
    increment =1.5
    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
        self.increment=sai/self.salary
e=Employee()
print(e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement=6000
print(e.increment)