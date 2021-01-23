requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'{requested_topping.title()} has been added to your pizza')
    print('Finished making your pizza')
else:
    print('Are you sure that you want you pizza blank?')            