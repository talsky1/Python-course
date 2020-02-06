
print("Guess number game")


import random

number = random.randint(0,10)
guess = int(input("Guess a number from 0 to 10 , type your guess here : "))
            
while True:
    if guess == number:
        break
    else:
        guess = int(input("Try again : "))

print("You guessed it , the number is", number)            
