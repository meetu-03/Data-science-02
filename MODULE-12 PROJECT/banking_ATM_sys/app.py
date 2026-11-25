
from logic import *

print("===== ABC BANK ATM =====")

if check_pin():

    while True:

        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:

            check_balance()

        elif choice == 2:

            withdrwal_ammount()

        elif choice == 3:

    
            deposit_amount()

        elif choice == 4:

            print("Thank You For Using ABC Bank ATM!")
            break

        else:

            print("Invalid Choice!")
