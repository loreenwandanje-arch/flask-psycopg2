
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
# person1.talk()
# person1.codes()

# person2 = Person("Jane", 24, 'jane@gmail.com', 'Syokimau')
# print(type(person2))
# print(person2.address)

# person2.work()
# person2.talk()
# person2.codes()

# # Task Create a class called BankAccount with the following attributes: -account number - balance - owner name - date opened
# # Create a class called BankAccount with the following attributes: -account number -balance -owner name -date opened 2.Give the above BankAccount
# # class the following behaviour or methods: -deposit() -withdraw() -display_info() 3.Create two BankAccount objects that can deposit, withdraw and display_info

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

# 1.Create a Car Class Have the following attributes brand - model - year -fuel_capcity - 
# fuel_level -is_running(boolen value) Have the following methods as behaviour for your 
# class: start() stop() refuel() drive() display_car_info()
from datetime import date

today = date.today()
print(today)

class Car:
    def __init__(self, brand, model, year, fuel_capacity, fuel_level):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capacity  
        self.fuel_level = fuel_level      
        self.is_running = False             

    def start(self):
        if self.is_running:
            print(f"{self.brand} {self.model} is already running!")
        else:
            self.is_running = True
            print(f"{self.brand} {self.model} has started.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} has stopped.")
        else:
            print(f"{self.brand} {self.model} is already stopped!")

    def refuel(self, amount):
        if self.fuel_level >= self.fuel_capacity:
            print("Tank is already full! No need to refuel.")
        elif self.fuel_level / self.fuel_capacity < 0.20:
            self.fuel_level = min(self.fuel_level + amount, self.fuel_capacity)
            print(f"Warning: Low fuel! Refuelled. Level now: {self.fuel_level}L")
        else:
            self.fuel_level = min(self.fuel_level + amount, self.fuel_capacity)
            print(f"Refuelled. Fuel level now: {self.fuel_level}L")

    def drive(self):
        if not self.is_running:
            print("Start the car first before driving!")
        elif self.fuel_level <= 0:
            print("No fuel! Please refuel before driving.")
        else:
            self.fuel_level -= 5
            print(f"{self.brand} {self.model} is driving! Fuel left: {self.fuel_level}L")

    def display_car_info(self):
        status = "Running" if self.is_running else "Stopped"
        print(f"- Car Info -")
        print(f"Brand      : {self.brand}")
        print(f"Model      : {self.model}")
        print(f"Year       : {self.year}")
        print(f"Fuel Cap   : {self.fuel_capacity}L")
        print(f"Fuel Level : {self.fuel_level}L")
        print(f"Status     : {status}")


#  Car 1: Honda Civic 
Car1 = Car("Honda", "Civic", 2022, 47, 30)
print(type(Car1))
print(Car1.brand)
Car1.start()
Car1.stop()
Car1.refuel(10)
Car1.drive()
Car1.display_car_info()

# --- Car 2: Nissan Altima ---
Car2 = Car("Nissan", "Altima", 2021, 60, 5)
print(type(Car2))
print(Car2.brand)
Car2.start()
Car2.stop()
Car2.refuel(20)
Car2.drive()
Car2.display_car_info()

# --- Car 3: Tesla Model 3 ---
Car3 = Car("Tesla", "Model 3", 2023, 70, 70)
print(type(Car3))
print(Car3.brand)
Car3.start()
Car3.stop()
Car3.refuel(10)
Car3.drive()
Car3.display_car_info()