#Permamently list sorting

cars = ['subaru', 'audi', 'isuzu', 'bmw', 'mitsubishi']
print('\n')
print('### Original list ###')
print(cars)
print('\n')
print('### Alphabetical list ###')
cars.sort()
print(cars)
print('\n')
print('### Reverse - Alphabetical list ###')
cars = ['subaru', 'audi', 'isuzu', 'bmw', 'mitsubishi']
cars.sort(reverse=True)
print(cars)

#Temporarily list sorting
print('\n')
print('### Temporarily sorting ###')
print(cars) # Original list
print(sorted(cars))
print(f"Printining again original cars list: {cars}")
#Reverse sorting
print('\n')
print('### Reverse ###')
print(cars)
cars.reverse()
print(cars)
