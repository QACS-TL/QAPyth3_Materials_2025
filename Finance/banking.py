#! /bin/python
# Name:        banking.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This module defines several functions for banking app.
"""
    Manages Bank accounts with deposits and withdrawals.
"""
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

def main():
    """ Withdraw and deposit monies """
    bank_balance = 0
    print(f"Welcome to mBA (mini Bank Account) App")

    while True:
        menu = f"""
                mBA Menu
                --------
                Current Balance {bank_balance}
                1. Deposit monies.
                2. Withdraw monies.   
        """
        print(menu)
        option = input("Enter option (1-2, q=quit): ")
        if option == "1":
            bank_balance = deposit(bank_balance)
        elif option == "2":
            bank_balance = withdraw(bank_balance)
        elif option.lower() == "q":
            break
        else:
            print("Invalid option")

    print("Thanks for using the mBA app.")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)

