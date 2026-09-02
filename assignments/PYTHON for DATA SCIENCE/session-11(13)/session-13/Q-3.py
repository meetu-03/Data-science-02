#Create a Paytm cashback calculator that asks for total spend and number of offers applied, then divides spend by offers to show average cashback per offer. If the number of offers is zero, raise a custom exception called NoOffersApplied and display a custom error message.



class NoOffersApplied(Exception):
    pass

def cashback_calculator(spend, offers):
    try:
        if offers == 0:
            raise NoOffersApplied("No offers were applied.")
        print(spend / offers)
    except NoOffersApplied as e:
        print(e)

cashback_calculator(1000, 5)
cashback_calculator(1000, 0)