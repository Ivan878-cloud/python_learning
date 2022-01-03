#=======Diction 2============




enemy = {
    'loc_x': 50,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudak',
}

all_enemies = []

all_enemies.append(enemy)
all_enemies.append(enemy)
all_enemies.append(enemy)

for x in range(0, 10):
    all_enemies.append(enemy.copy())
for ene in all_enemies:
    print(ene)

#====change parametres======

    print("===================\n=====================\n")

all_enemies[5]['health'] = 30
all_enemies[4]['name'] = 'superMudak'
all_enemies[6]['loc_x'] += 100

for ene in all_enemies:
    print(ene)

