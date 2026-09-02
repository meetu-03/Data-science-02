#Use iter() and next() to manually loop through a list of your 5 favorite food delivery apps (like Zomato, Swiggy, Domino's, etc.) and print each app name one by one.

apps = ["Zomato", "Swiggy", "Domino's", "Uber Eats", "EatSure"]

app_iterator = iter(apps)

while True:
    try:
        app = next(app_iterator)
        print(app)
    except StopIteration:
        break