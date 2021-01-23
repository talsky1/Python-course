aviabled_toppings = ['olives', 'mushrooms', 'paper', 'tuna', 'tomato']
requested_toppings = ['tomato', 'mushrooms', 'peperoni']
for requested_topping in requested_toppings:
    if requested_topping in aviabled_toppings:
        print(f'{requested_topping.title()} has been added to the pizze')
    else:
        print(f'I am sorry, i dont have {requested_topping.title()}')    
print("\nYour pizza is ready!")        