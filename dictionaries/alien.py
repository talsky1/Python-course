
alien_0 = {'color': 'green', 'points': '5'}
print(alien_0['color'])
print(alien_0['points'])
alien_0['x_pos'] = 0
alien_0['y_pos'] = 25
alien_0['speed'] = 'medium'
print(f"Alien`s original position is {alien_0['x_pos']}.")
# print(alien_0)
# print('\n')
# print(f"The alien`s color is {alien_0['color'].upper()}")
# alien_0['color'] = 'red'
# print('\n')
# print(f"The alien`s new color is {alien_0['color'].upper()}")
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_pos'] = alien_0['x_pos'] + x_increment          
print(f"\nAlien`s new position is {alien_0['x_pos']}.(based on alien`s speed).")
print(alien_0)
del alien_0['points']
print(alien_0)
points_value = alien_0.get('points', 'You dont have any points')
print(points_value)