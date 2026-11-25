
balance = 50000
pin = 131406
daily_deposite = 0


def check_pin():

    for i in range(3):

        entered_pin = int(input("ENTER YOUR PIN: "))

        if entered_pin == pin:
            print("****** WELCOME TO ABC BANK ATM ******")
            return True

        else:
            print("Wrong PIN!")

    print("ATM BLOCKED!")
    return False


def check_balance():
    print("Your Balance Is:", balance)


def withdrwal_ammount():

    global balance

    amount = int(input("ENTER WITHDRAWAL AMOUNT: "))

    if amount <= 0:
        print("INVALID AMOUNT!")

    elif amount <= balance:
        balance -= amount
        print("WITHDRAWAL SUCCESSFUL!")
        print("YOUR CURRENT BALANCE:", balance)

    else:
        print("INSUFFICIENT BALANCE!")


def deposit_amount():

    global balance, daily_deposite

    amount = int(input("ENTER DEPOSIT AMOUNT: "))

    if amount <= 0:
        print("INVALID AMOUNT!")

    elif daily_deposite + amount <= 50000:

        balance += amount
        daily_deposite += amount

        print("DEPOSIT SUCCESSFUL!")
        print("DEPOSIT AMOUNT:", amount)
        print("YOUR CURRENT BALANCE:", balance)
        print("YOUR DAILY DEPOSIT LIMIT REMAINING:", 50000 - daily_deposite)

    else:
        print("DAILY DEPOSIT LIMIT EXCEEDED!")
        print("REMAINING LIMIT:", 50000 - daily_deposite)
