#Create a function format_followers that takes a number and returns it in 'K' or 'M' format (e.g., 1500 → '1.5K', 1200000 → '1.2M'), then use map() to apply it to a list of follower counts: [950, 1500, 25000, 1200000].

def formatee_follower(number):
    if number >=1000000:
        return str(number/1000000) + "m"
    elif number >= 1000:
        return str(number/1000) + "k"
    else:
        return str(number)

followers = [950, 1500, 25000, 1200000]

result = list(map(formatee_follower, followers))

print(result)    