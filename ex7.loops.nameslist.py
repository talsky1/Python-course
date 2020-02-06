print("Random name from list")

import random

people = []
for x in range(0,8):
    names = input("Type 8 names, one of them going to be printed at the end: ")
    people.append(names)

index = random.randint(0,7)
random_person = people[index]

print("Random person is:",random_person)

    
        
