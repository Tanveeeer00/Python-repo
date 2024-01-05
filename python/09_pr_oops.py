# create a class programmer for storing information of few programmers working at microsoft
class Programmer:
    company = "Google"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getinfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")
kaif=Programmer("Kaif","Skype")
aika=Programmer("Aika","Github")
kaif.getinfo()
aika.getinfo()

# Write a class calculator capable of finding square,cube and squareroot of a number and add static method to greet the user with hello
class Calculator:
    def __init__(self,num):
        self.number=num
    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")
    def squareRoot(self):
        print(f"The value of {self.number} square is {self.number **0.5}")
    def cube(self):
        print(f"The value of {self.number} square is {self.number **3}")
    @staticmethod
    def greet():
        print("hello there welcome to the best calculator of the world")
a = Calculator(9)
a.square()
a.squareRoot()
a.cube()
a.greet()

# Create a class with a class attribute b; create an object from it and set a directly using object b=0.Does the change the class attribute
class sample:
    b="harry"
obj=sample()
obj.b="Vikky"
sample.b="ricky" #it create instance attribute and class attribute cannot change,output give return value with instance attribute 

print(sample.b)
print(obj.b)

# Write a class train which has methods to book a ticket,get status (no. of seats) and get fare information of train running under Indian Railways
class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def  getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat no. is {self.seats}")
            self.seats=self.seats - 1
        else:
            print(f"Sorry this train is full! kindly try in tatkal")
    
    def cancelTicket(self,seatNo):
        pass

intercity=Train("Intercity Express:15402",90,2)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.getStatus()

# Can you change the self parameter inside a class to something else (say "harry"). Try changing self to "slf" or "harry" and see the effects
class Change: 
    def __init__(slf, name):
        slf.name = name

obj = Change("Harry") 
print(obj.name) 
 