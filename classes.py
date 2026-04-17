
# class Person:
#     def __init__(self, name, age, email, address):
#         self.name = name
#         self.age = age
#         self.email = email
#         self.address = address

#     def work(self):
#         print(f"{self.name} works")

    
#     def talk(self):
#         print(f"{self.name} talks")

    
#     def codes(self):
#         print(f"{self.name} codes")


# person1 = Person("Ceaser", 30, 'belongstoceaser@gmail.com', 'Athiriver')
# print(type(person1))
# print(person1.address)

# person1.work()
# person1.talks()
# person1.codes()

# person2 = Person("Jane", 24, 'jane@gmail.com', 'Syokimau')
# print(type(person2))
# print(person2.address)

# person2.work()
# person2.talks()
# person2.codes()

# Task Create a class called BankAccount with the following attributes: -account number - balance - owner name - date opened
# Create a class called BankAccount with the following attributes: -account number -balance -owner name -date opened 2.Give the above BankAccount
# class the following behaviour or methods: -deposit() -withdraw() -display_info() 3.Create two BankAccount objects that can deposit, withdraw and display_info

# from datetime import datetime

# today = datetime.today().date()

# class BankAccount:
#     def __init__ (self,account_number,balance,owner_name,date_opened= today):
#         self.account_number = account_number
#         self.balance = balance
#         self.owner_name = owner_name
#         self.date_opened = date_opened

#     def deposit(self):
#         print(f"{self.owner_name} deposit confirmed!")

#     def withdraw(self):
#         print(f"{self.owner_name} withdrawal made!")   

#     def display_info(self):
#         print(f"{self.owner_name}, -{self.date_opened}, -{self.balance},-{self.account_number} display transaction information")        


# today = datetime.today().date()
# print(today)

# account1 = BankAccount(456789,1000000,"Kerry Ortiz")
# print(type(account1))
# print(account1.owner_name)

# account1.deposit()
# account1.withdraw()
# account1.display_info()

# account2 = BankAccount(123098,9000,"Sade Kabue")
# print(type(account2))
# print(account2.owner_name)

# account2.deposit()
# account2.withdraw()
# account2.display_info()

from datetime import datetime

today = datetime.today().date()

class Car:
    def __init__(self,brand,model,fuel_capacity,fuel_level,is_running,year=today):
        self.brand = brand
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_level
        self.is_running = is_running
        self.year = year

    def start (self):
        print(f"{self.brand},-{self.model} starts at 0km/h")
    def stop (self):
        print(f"{self.brand},-{self.model} stops at 70km/h")
    def refuel (self):
        print(f"{self.brand},-{self.model} refuel before 20%!")
    def drive(self):
        print(f"{self.brand},-{self.model} drive!")
    def display_car_info(self):
        print(f"{self.brand},-{self.model},-{self.fuel_capacity},-{self.fuel_level},is running at {self.is_running},-{self.year}")        


today = datetime.today().date()
print(today)

Car1 = Car("Honda","Civic",'47 Litres','87 Octane(Regular)','90Km/h')
print(type(Car1))
print(Car1.brand)

Car2 = Car("Nissan","Altima",'60 Litres','87 Octane(Regular)','110Km/h')
print(type(Car2))
print(Car2.brand)

Car3 = Car("Tesla","Model 3",'70 Kw/h','100%','201Km/h')
print(type(Car3))
print(Car3.brand)

Car4 = Car("Toyota","Camry",'60 Litres','87 Octane(Regular)','190Km/h')
print(type(Car4))
print(Car4.brand)
 
Car1.start()
Car1.stop()
Car1.refuel()
Car1.drive()
Car1.display_car_info()

Car2.start()
Car2.stop()
Car2.refuel()
Car2.drive()
Car2.display_car_info()

Car3.start()
Car3.stop()
Car3.refuel()
Car3.drive()
Car3.display_car_info()

Car4.start()
Car4.stop()
Car4.refuel()
Car4.drive()
Car4.display_car_info()

