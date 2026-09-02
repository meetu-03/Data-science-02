#Build a recursive function format_number_short(n) that takes a number (like a follower count on Instagram or YouTube) and returns it as a string in short format: 1500 as '1.5K', 1200000 as '1.2M', 500 as '500'.


def formate_number_short(n):
  if  n >= 1000000:
    return str(n/1000000) + "m"
  elif n >= 1000:
    return str(n/1000) + "k"
  else:
    return str(n)


print(formate_number_short(1500))
print(formate_number_short(135053))
print(formate_number_short(123))

