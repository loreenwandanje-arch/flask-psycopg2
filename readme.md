OOP CONCEPTS
1.Inheritance-A child class gets all features of the parent class.
# parent class
class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname (self):
        print(self.firstname,self.lastname)

x = Person("John", "Doe")
x.printname()

# child class
class Student(Person):
  pass
x = Student("Mike", "Olsen")
x.printname()
# Now the Student class has the same properties and methods as the Person class.

2.Encapsulation-Hiding data inside a class and controlling access to it.
class Product:
    def __init__(self, name, buying_price, selling_price):
        self.name = name
        self.__buying_price = buying_price  # private - hidden with __
        self.selling_price = selling_price  # public - anyone can see

    # controlled way to access buying price
    def get_buying_price(self):
        return self.__buying_price

    def get_profit(self):
        return self.selling_price - self.__buying_price

