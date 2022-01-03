
#============Объекты=================


#==============

#=========ITEM====================
#====keys====values====================
enemy = {
    'loc_x': 50,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudak',
}
print(enemy)

print("Location X = " + str(enemy['loc_x']))
print("Location Y = " + str(enemy['loc_y']))
print("His name is " + enemy['name'])


enemy['rank'] = 'General'
print(enemy)

del enemy['rank']
print(enemy)

enemy['loc_x'] = enemy['loc_x'] + 40
enemy['health'] = enemy['health'] - 50
if enemy['health'] < 80:
    enemy['color'] = 'yellow'

print(enemy)

print(enemy.keys())
print(enemy.values())
