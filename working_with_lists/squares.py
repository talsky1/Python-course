#V1
squares = []
for value in range(1,11):
	square = value ** 2
	squares.append(square)
print(squares)	

#V1.1
squares = []
for value in range(1,11):
	squares.append(value ** 2 )
print(squares)	
print( sum(squares) )
print( min(squares) )
print( max(squares) )

#Test v1.2
numbers = []
for number in range(1,1000000):
	numbers.append(number)
print( sum(numbers) )
print( min(numbers) )
print( max(numbers) )

#One line squares
squares = [value ** 2 for value in range(1,11)]
print(squares)
