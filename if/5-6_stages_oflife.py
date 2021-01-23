age = int(input("Please type what is your age: "))
if age < 2:
    print("You are baby")
elif age < 4:
    print("You are a toddler")
elif age < 13:
    print("You are a kid")
elif age == 13 or age < 20:
    print("You are teenager")
elif age == 20 or age < 65:
    print("You are adult")
else:
    print("You are elder")            