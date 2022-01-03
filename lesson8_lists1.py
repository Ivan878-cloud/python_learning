#============Массивы==============


cities = ['Moscow', 'Piter', 'Krasnogorsk', 'Kirov', 'Abakan', 'abaza']

print(len(cities))
print(cities)
print(cities[-1])
print(cities[-1].title())
print(cities[1].upper())

cities[5] = 'Krasnoyarsk'
print(cities)

cities.append('Kursk')
print(cities)

cities.insert(0,'Mezhdura')
print(cities)

del cities[-2]
print(cities)

cities.remove('Mezhdura')
print(cities)

deleted_city = cities.pop()
print(deleted_city)
print(cities)

cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)

cities.reverse()
print(cities)

