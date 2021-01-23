print("String test: ")
car = 'scoda'
if car == 'scoda':
    print(bool(car))
print("\nlower() method")
car = 'BmW'
if car.lower() == 'bmw':
    print(bool(car))
print('Numbers test\n')
number = 10
if number == 10:
    print(bool(number))
if number != 20:
    print(bool(number))
if number > 50:
    print(bool(number)) 
if number < 11:
    print(bool(number)) 
if number >= 15:
    print(bool(number))  

print("\nList test") 
numbers_list = ['5', '6', '11', '15']
number = '5'
if number in numbers_list:
    print(f"Number {number} is in list")  
number2 = '20' 
if number2 not in numbers_list:
    print(f"Number {number2} is not in list")                               