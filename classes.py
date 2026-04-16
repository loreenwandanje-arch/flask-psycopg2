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
class BankAccount:
    def __init__(self,account_number,balance,owner_name,date_opened):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened

    def deposit(self):
        print(f"{self.owner_name} deposit confirmed!")

    def withdraw(self):
        print(f"{self.owner_name} withdrawal made!")   

    def display_info(self):
        print(f"{self.owner_name} display transaction information")        

account1 = BankAccount(456789,1000000,"Kerry Ortiz","10/04/2026")
print(type(account1))
print(account1.owner_name)

account1.deposit()
account1.withdraw()
account1.display_info()

account2 = BankAccount(123098,9000,"Sade Kabue","10/05/2026")
print(type(account2))
print(account2.owner_name)

account2.deposit()
account2.withdraw()
account2.display_info()