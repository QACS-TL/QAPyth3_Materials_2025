#! /bin/python
# Name:        account.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This is MBA - Minions Banking App used by millions of minions!.
"""
    Withdraw, Deposit and Display banking information.
"""

import sys
# import banking
import QATraining
import banking
#from banking import withdraw
#from banking import deposit
#from banking import withdraw
#from QATraining import deposit
#from QATraining import deposit
#from QATraining import withdraw

def display_info(bal, scode):
    """ Display bank account info """
    print(f"Current balance = £{bal:.2f}, sort code = {scode}")
    return None

def main():
    """ Withdraw, deposit and display bank account information """
    bank_balance = 34_500.23
    sort_code = "80-45-37"

    print("Welcome to MBA - Minions Banking App")
    name = input("Enter your name: ").title()
    while True:
        menu = f""" 
            Menu Options
            ------------
            1. Display Balance
            2. Deposit monies
            3. Withdraw monies
        """
        print(menu)
        option = input("Enter option (1-3, q=quit): ")
        if option == "1":
            display_info(bank_balance, sort_code)
        elif option == "2":
            bank_balance = QATraining.deposit(bank_balance)
        elif option == "3":
            bank_balance = banking.withdraw(bank_balance)
            # QATraining.deposit(100)
        elif option.lower() == "q":
            break
        else:
            print("Invalid option")

    print(f"Thank you {name} for using our app!")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
