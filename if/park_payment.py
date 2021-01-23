# age = 5
# if age <= 4:
#     print("The entry is free for age younger than 4")
# elif age < 18:
#     print("The entry fee is 25$")
# else:
#     print("Entry fee for age 18+ is 40$")    

age = 5
if age <= 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"The entry fee is {price}$")    