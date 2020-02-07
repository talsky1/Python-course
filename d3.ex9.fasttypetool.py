#07/02/2020 day3
import matplotlib.pyplot as plt
import time as t

times = []
mistakes = 0

print("Learn how to type faster , you will have to type the word 'sababa' as fast as u can for 5 times")
input("Press enter to continue.")

while len(times) < 5:
    start = t.time()
    word = input("Type the word: ")
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)
    if (word.lower() != "sababa"):
        mistakes += 1
        
print("You made" , str(mistakes) , "mistake(s).")
print("Now let`s see your evolution")

t.sleep(2)

x = [1, 2, 3, 4, 5]
y = times
legend = [ "1" , "2" , "3", "4", "5" ]

plt.xticks(x,legend)
plt.ylabel("Time in seconds")
plt.xlabel("Tryes")
plt.title("Your typing evolution")
plt.plot(x,y)
plt.show()


    

