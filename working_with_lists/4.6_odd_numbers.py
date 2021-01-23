#4.6 odd numbers
numbers = list( range(1,21,2) )
print(numbers)

#4.7 Threes
numbers = [number * 3 for number in range(3,31)]
print(numbers)

#4.8 Cubes
numbers = []
for number in range(1,11):
	numbers.append(number ** 3 )
print(numbers)	


#4.8.1
numbers = [number ** 3 for number in range(1,11)]
print(numbers)