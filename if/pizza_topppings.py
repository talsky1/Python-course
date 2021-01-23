requested_toppings = ['mushrooms', 'tomato', 'olives']
for requested_toping in requested_toppings:
    if requested_toping == 'test':
        print('Sorry we dont have tomato')
    else:
        print(f'{requested_toping} has been added to your pizza')
print('Your pizza is ready')            