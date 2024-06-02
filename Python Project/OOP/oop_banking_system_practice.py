import json

class User:
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
    def __init__(self, name, age, gender, balance):
        super().__init__(name, age, gender)
        self.balance = balance

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
        if account.name == name:
            return account
    return None

# this would output a main object, and append it into a list
def load_accounts(account_data):
    bank_accounts = []
    for account in account_data:
        name = account['name']
        age = account['age']
        gender = account['gender']
        balance = account['balance']
        bank_account = Bank(name, age, gender, balance)
        bank_accounts.append(bank_account)
    return bank_accounts

# Read the account details from JSON file
with open("account_details.json", "r") as file:
    data = json.load(file)
bank_accounts_dict = data["bank_accounts"]

# Load the accounts into a list
# bank_accounts is a list with class bank main object
bank_accounts = load_accounts(bank_accounts_dict)

while True:
    print("Welcome to the Banking System")
    # Allow users to modify their accoun balance
    input_name = input("Please enter your name: ")
    user_acc = get_account_by_name(input_name)

    if user_acc:
        print(f"Welcome {input_name}!")
        print("What would you like to do?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = int(input("How much would you like to deposit? "))
            user_acc.deposit(amount)
        elif choice == 2:
            amount = int(input("How much would you like to withdraw? "))
            user_acc.withdraw(amount)
        elif choice == 3:
            user_acc.show_balance()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")
    else:
        response = input("Account not found. Do you want to ope a new account? (Y/N)")
        if response.lower() == "y":
            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            gender = input("Enter your gender: ")
            balance = int(input("How much you would like to deposit now? "))
            user_acc = Bank(name, age, gender, balance)
            bank_accounts.append(user_acc)
            break
        else:
            break

# Here is 2 way to modify the JSON file
# Update the JSON file
# data["bank_accounts"] = [account.__dict__ for account in bank_accounts]
# Update the JSON file
updated_data = {"bank_accounts": []}
for account in bank_accounts:
    account_data = {
        "name": account.name,
        "age": account.age,
        "gender": account.gender,
        "balance": account.balance
    }
    updated_data["bank_accounts"].append(account_data)

with open("account_details.json", "w") as file:
    json.dump(updated_data, file, indent=4)
    print("JSON file updated successfully!")


print("Thanks for using our service.")

# user1 = User("sam", 18, "M")
# User.show_details(user1)
# user1.show_details()