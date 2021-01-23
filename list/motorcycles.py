motorcycles = ['honda', 'kawasaki', 'suzuki', 'bmw']
print(motorcycles[-1].title())

#Change value in the list
motorcycles[-1] = 'testsky'
print(motorcycles[-1].title())
print(motorcycles)

#Append value to the list
motorcycles.append('bmw')
print(motorcycles)

#Insert value to the list
motorcycles.insert(0, 'harley')
print(motorcycles)

#Remove value from the list
del motorcycles[1]
print(motorcycles)

#Remove value by using pop() method
popped_motorcyle = motorcycles.pop()
print(motorcycles)
print(popped_motorcyle)
last_owned = motorcycles.pop()
message = f"My last owned motorcycle is {last_owned.title()}"
print(message)
print(motorcycles)
first_owned = motorcycles.pop(0)
message = f"My first owned motorcycle was {first_owned.title()}"
print(message)

#Remove value from the list by value name
print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)