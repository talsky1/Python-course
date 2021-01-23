pizza_list = ['tuna', 'tomato', 'olives']
for pizza in pizza_list:
	print(f"I really like pizza with {pizza}")
print(f"My favorite pizza is pizza with {pizza_list[0]}\nalso i like to add to this pizza some {pizza_list[1]}\nand a litle {pizza_list[-1]}.\nI really love pizza!!!")	

friend_pizzas = pizza_list[:]
pizza_list.append('empty')
friend_pizzas.append('sumsum')
print(f'my favorite pizzas are:')
for pizza in pizza_list:
	print(pizza.title())
print(f'\nMy friends favorite pizza is:')
for pizzas in friend_pizzas:
	print(pizzas.title())
print('\nThis pizzas are my and my friend`s favorites')	