pets = ['king', 'bony', 'gera', 'sky', 'tofi']
print(f"Here are all my pets that i ever had: {pets}")
print(f"Total number of pets that i had is: {len(pets)}")
cat = pets.pop(4)
print(f"{cat.title()} is a cat, all the rest are dogs thats why i removed her from the list")
pets.append('ava')
print(pets)
print(f"Last dog in the list is my father`s dog, and she`s name is: {pets[4].title()}")
pets.remove('ava')
print(f'Now i`ll remove from my list my father`s dog: {pets}.\nThis list is sorted from 1st to last pets')
pets.sort()
print(f"Now i`ll show you my pets sorted by alphabet: {pets}")
pets.sort(reverse=True)
print(f"And now my pets list is reversed: {pets}")
print(f'Temorarily sorted list: {sorted(pets)} \nAnd now original list again{pets}')



