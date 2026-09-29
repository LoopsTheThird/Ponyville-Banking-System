import validator as valid
class Bank:
    def __init__(self):
        self.accounts = []

    def find_account(self, number):
        for account in self.accounts:
            if account.number == number:
                return account

    def create_account(self, name, number, pin):

        if self.find_account(number):
            return False
        
        account = Account(name, number, pin, balance=0)

        self.accounts.append(account)

        return True

    def delete_account(self, number):
        for account in self.accounts:
            if account.number == number:
                self.accounts.remove(account)
                print("Account deleted successfully.")
                return True

        print("Account not found.")
        return False

    def login(self, number, pin):
        for account in self.accounts:
            if account.number == number and account.pin == pin:
                return account, True

        print("Invalid account number or pin. Please try again.")
        return False
            
class Account:
    def __init__(self, name, number, pin, balance):
        self.name = name
        self.number = number
        self.pin = pin
        self.balance = balance

    def __str__(self):
        return (
            f"Account Number: {self.number}\n"
            f"Name: {self.name}\n"
            f"Balance: {self.balance}"
        )

    def withdraw(self, amount):
        if amount < self.balance:
            original_balance = self.balance
            self.balance -= amount
            withdrawal_balance = original_balance - amount
            print(f"""=============== Withdrawal Details ===============
Status: Successful
Amount of withdrawal = ${amount}
New Balance = ${original_balance} - ${amount} = {withdrawal_balance}""")
            return True

        else:
            print(f"Withdrawal amount of {amount} exceeds account [{self.number}]'s balance of {self.balance}")
            return False


    def deposit(self, amount):
        if amount < 0:
            print(f"Deposit amount of {amount} is invalid. Please enter a positive amount.")
            return False

        if amount > 10000:
            print(f"Deposit amount of {amount} exceeds the maximum limit of $10000.")
            return False

        original_balance = self.balance
        self.balance += amount
        deposit_balance = original_balance + amount
        print(f"""=============== Deposit Details ===============
Status: Successful
Amount of Deposit = ${amount}
New Balance = ${original_balance} + ${amount} = {deposit_balance}""")
        
        return True