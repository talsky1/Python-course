guests = ['tal', 'ofri', 'yahel', 'sky']
message = f"Hello dear {guests[0].title()}, how are you today?"
print(message)
message = f"Hello dear {guests[1].title()}, how are you today?"
print(message)
message = f"Hello dear {guests[2].title()}, how are you today?"
print(message)
message = f"Hello dear {guests[3].title()}, how are you today?"
print(message)
print('\nOhhhh YEAHHH!! i have found bigger table and i can invite Tofi , bla and blu')
guests.append('tofi')
guests.insert(0, 'bla')
guests.insert(3, 'blu')
print(f"Here is my new list of guests: {guests}")
message = f"Hello dear {guests[0].title()}, how are you today?"
print(message)
message = f"Hello dear {guests[1].title()}, how are you today?"
print(message)
message = f"Hello dear {guests[2].title()}, how are you today?"
print(message)
message = f"Hello dear {guests[3].title()}, how are you today?"
print(message)
message = f"Hello dear {guests[4].title()}, how are you today?"
print(message)
message = f"Hello dear {guests[5].title()}, how are you today?"
print(message)
message = f"Hello dear {guests[6].title()}, how are you today?"
print(message)
print("i didnt got my damn table so i will be able to invite only 2 guests")
first_popped = guests.pop(6)
print(f"Sorry {first_popped.title()}, i dont have enough space arround my table.")
second_popped = guests.pop(5)
print(f"Sorry {second_popped.title()}, i dont have enough space arround my table.")
third_popped = guests.pop(4)
print(f"Sorry {third_popped.title()}, i dont have enough space arround my table.")
fourth_popped = guests.pop(3)
print(f"Sorry {fourth_popped.title()}, i dont have enough space arround my table.")
fifth_popped = guests.pop(2)
print(f"Sorry {fifth_popped.title()}, i dont have enough space arround my table.")
print(f"I can invite only {guests}")



