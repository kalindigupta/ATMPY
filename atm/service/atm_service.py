from models import account

def show_balance():
    print("Balance =", account.balance)

def deposit():
    amount = int(input("Enter amount: "))
    account.balance += amount
    account.transactions.append(f"Deposited {amount}")

def withdraw():
    amount = int(input("Enter amount: "))

    if amount <= account.balance:
        account.balance -= amount
        account.transactions.append(f"Withdrawn {amount}")
    else:
        print("Insufficient Balance")

def show_statement():
    for t in account.transactions:
        print(t)