#2.Create a function called get_delivery_charge(amount, city='Ahmedabad') that returns 0 if city is 'Ahmedabad', otherwise returns 50 as a delivery charge.<br><br><em><strong>Hint:</strong> Use a default argument for the city parameter.</em>



def get_delivary_charge(amount,city="ahmdabad"):
    if city == "ahmdabad":
        return 0
    else:
        return 50
print(get_delivary_charge(500))
print(get_delivary_charge(500,"morbi"))
