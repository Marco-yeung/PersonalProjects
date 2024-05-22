class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Bank details")
        print(f"Welcome {self.name}")
        print(f"You are {self.age} years old")
        print(f"Gender: {self.gender}")

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f"Account balance has been updated: {self.balance}")

    def withdraw(self, amount):
        self.amount = amount
        if self.balance < self.amount:
            print("Insufficient balance to withdraw")
            print(f"Your balance: {self.balance}")
        else:
            self.balance = self.balance - self.amount
            print(f"Account balance has been updated: {self.balance}")

    def show_balance(self):
        self.show_details()
        print(f"Balance: {self.balance}")

def get_account_by_name(name):
    for account in bank_accounts:
        if account['name'] == name:
            return account
        return None


bank_accounts = [Bank("Ann", 25, "F"),
                 Bank("Bob", 40, "M")]
                 
        
while True:
    print("Welcome to the Banking System")
    # Allow users to modify their accoun balance
    input_name = input("Please enter your name: ")
    user_acc = get_account_by_name(input_name)
    print(f"Welcome {input_name}! ")
    print("What would you like to do?")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")
    # here if user_acc is not null
    if user_acc:
        choice = int(input("What would you likt to do"))
        if choice == 1:
            amount = int(input("How much would you likt to deposit?"))
        




# user1 = User("sam", 18, "M")
# User.show_details(user1)
# user1.show_details()