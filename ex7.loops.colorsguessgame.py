print("Guess the color!")

import random

colors_list = ["green", "white", "yellow","red","blue","black"]

while True:
    color = colors_list[random.randint(0,len(colors_list))-1]
    guess = input("Your guess is : ").lower
    
    while True:
        if(color == guess):
            break
        else:
            guess = input("try again: ")
            
    print("You guessed it! the color is:", color)
    keep_playing = input('Type "No" if you want to stop playing: ').lower
    if keep_playing() == "no":
        break
    
print("Game Over")        
     


        
        
    
        
        

