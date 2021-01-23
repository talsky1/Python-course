my_food = ['antrikot', 'lamb', 'meat', 'sea food']
friends_food = my_food[:]
my_food.append('fruits')
friends_food.append('vegetables')
print('This is the food that i like:')
print(my_food)
print('\nAnd here is my friends favorite food list:')
print(friends_food)
#4-10
print(f'The first 3 items in the list are {my_food[:3]}')
print(f'3 items in the middle of the list are {my_food[1:4]}')
print(f'The last 3 items in the list are {my_food[-3:]}')

#4-12
for food in my_food:
	print(f'I really like {food.title()}')
print('\n')	
for dish in friends_food:
	print(f'This is my friends favorite food: {dish.title()}')

