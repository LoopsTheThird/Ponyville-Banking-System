import time

accounts = {
    "account_1" : {
        "number": "000000",
        "pin" : "0000",
        "name" : 'w',
        "balance" : 20000
    },
    "account_2" : {
            "number": "000000",
            "pin" : "0000",
            "name" : 'w',
            "balance" : 20000
        }
}

def transfer(account_number, reciver_number, amount):
    for account in accounts:
                if account[account]["number"] == reciver_number:
                        original_balance = accounts[account]["balance"]
                        if amount <= 10000:
                                new_balance = original_balance + amount
                                accounts[account]["balance"] = new_balance
                                print(f"""===== Transfer Information [account ({account_number}) to account ({reciver_number})]=====
Transfer is successful!
Original Balance = {original_balance}
Transfer amount = {amount}
New Balance = {original_balance} + {amount} = {new_balance}""")
                                    
                                break
    
                        else:
                            print("Transfer amount exceeds $10000")
                            break
      
    print(f"No reciever acccount ({reciver_number}) found or an error happened")
     

def deposit(number, amount):
        for account in accounts:
                original_balance = accounts[account]["balance"]
                if amount <= 10000:
                            new_balance = original_balance + amount
                            accounts[account]["balance"] = new_balance
                            print(f"""===== Deposit Information [account ({number})]=====
Deposit is successful!
Original Balance = {original_balance}
Deposit amount = {amount}
New Balance = {original_balance} + {amount} = {new_balance}""")
                            break

                else:
                    print("Deposit amount exceeds $10000")
                    break



def withdraw(number, amount):
            for account in accounts:
                    original_balance = accounts[account]["balance"]
                    if amount <= 10000:
                        if amount <= original_balance:
                                new_balance = original_balance - amount
                                accounts[account]["balance"] = new_balance
                                print(f"""===== Withdrawal Information [account ({number})]=====
Withdrawal is successful!
Original Balance = {original_balance}
Withdrawal amount = {amount}
New Balance = {original_balance} - {amount} = {new_balance}""")
                                break

                        else:
                            print(f"Withdrawal amount of {amount} exceeds account balance of {original_balance}")
                    else:
                        print("Withdrawal amount exceeds $10000")
                        break
  
def controls(number, name):
    while True:
        try:
            user_input = int(input(f"""===== Account {number}, Hi {name}! =====
1. Check Balance
2. Deposit
3. Withdraw
4. Transfer
5. Logout
Please enter a number that corresponds with the action: """))

        except ValueError:
            print("Invalid input. Please Enter a number.")
            continue

        if user_input == 1:
            for account in accounts:
                if accounts[account]["number"] == number:
                    print(f"\nAccount balace of account {number} is ${accounts[account]['balance']}\n")

                else:
                    print("\nAccount number not found\n")

        elif user_input == 2:
            try:
                amount = int(input("Enter amount of deposition: $"))

            except ValueError:
                print("Enter amount in digits")

            else:
                if confirmation("Deposit", amount):
                    deposit(number, amount)

        elif user_input == 3:
            try:
                amount = int(input("Enter amount of withdrawal: $"))
        
            except ValueError:
                    print("Enter amount in digits")
        
            else:
                if confirmation("Withdraw", amount):
                    withdraw(number, amount)

        elif user_input == 5:
            print("Logging out...")
            break


def is_a_digit(var):
    if var.isdigit():
        return True
    
    else:
        print("\nPlease enter digits\n")
        return False

def length(var, length):
    if len(var) == length:
        return True
    
    else:
        return False

def negative(amount):
    if amount < 0:
        print("\nPlease enter a positive amount.\n")
        return True
    else:
        return False

def confirmation(type, amount):
        while True:
            user_confirm = input(f"{type}ing amount of {amount}, are you sure you want to continue? Type y for yes or n for no: ").lower()
            if user_confirm == 'y':
                print("Processing...")
                return True
            elif user_confirm == 'n':
                print("Withdrawal closed")
                return False
            else:
                print("Invalid option.")                      

def login(pin, number, name):
    for i in accounts:
        if accounts[i]["number"] == number and accounts[i]["pin"] == pin and accounts[i]["name"] == name:
            print("\nLogin successful!\n")
            return True

    print("\nLogin failed. Please check your account number, pin, and name.\n")
    return False

while True:
    try:
        user_input = int(input("""===== Banking System =====
1. Login
2. Create New Acount
3. Exit
Please enter a number that corresponds with the action: """))
    
    except ValueError:
        print("\nInvalid input. Please Enter a number.\n")

    else:
        if user_input == 1:

            account_number = input("Enter account number: ")

            if not is_a_digit(account_number):
                continue

            if not length(str(account_number), 6):
                print("Please enter a 6 digit account number.")
                continue

            account_pin = input("Enter account pin: ")

            if not is_a_digit(account_pin):
                continue

            if not length(str(account_pin), 4):
                print("\nPlease enter a 4 digit account pin.\n")
                continue

            account_name = input("Enter your name: ")

            if login(account_pin, account_number, account_name):
                controls(account_number, account_name)
                
        elif user_input == 2:
            pass

        elif user_input == 3:
            print("Exiting Program...")
            break

        else:
            print("\nInvalid input. Please try again with a number from 1-3.\n")