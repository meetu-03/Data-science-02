# 1.Write a Python script that takes your current Spotify listening time in minutes and checks if it is above 120 minutes; if yes, print 'You are a true music fan!', otherwise print 'Keep listening!'.

# ANSWER...

spotify_listening=int(input("enter your listening time in minuts:"))
if spotify_listening>120:
    print("you are true music lover")
else:
    print("keep listeining")

# 2.Create a Python program that asks the user to enter their Zomato order amount and checks if it is above 300; if yes, print 'Eligible for free delivery', else print 'Delivery charges apply'.

# ANSWER...

order_amount=int(input("enter your order amount"))
if order_amount>300:
    print("eligible for free delivery")
else:
    print("delivery charge apply")



# 3.Build a Python script that takes your Flipkart cart total and applies the following logic: if total > 2000, print 'You get a 10% discount'; elif total > 1000, print 'You get a 5% discount'; else print 'No discount available'.    

# ANSWER...

flipkart_total=int(input("enter your total"))
if flipkart_total>2000:
    print("you get a 10% discount:",flipkart_total*0.1)
elif flipkart_total>1000:
    print("you get 5% discount:",flipkart_total*0.05)
else:
    print("no discount available") 


# 4.Write a Python program that asks the user to enter their IPL fantasy team points and uses nested if-else statements to print: 'Champion' if points > 800, 'Top Performer' if points between 500 and 800, 'Keep Trying' otherwise.<br><br><em><strong>Hint:</strong> Use nested if-else blocks to check the ranges.</em>

# ANSWER...
           
points=int(input("enter you team's point"))
if points>800:
    print("champion")
else:
    if points>=500:
        print("top performer")
    else:
        print("keep trying") 
