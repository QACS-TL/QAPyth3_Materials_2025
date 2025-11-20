import sys

def deposit(balance):
    """ Deposit monies into bank account """
    amount = float(input("Please enter amount to be added: "))
    balance += amount
    print(f"Deposited {amount}.")
    return balance

def withdraw(balance):
    """ Withdraw monies from bank account """
    amount = float(input("Please enter amount to withdraw: "))
    balance -= amount
    print(f"{amount} withdrawn.")
    return balance