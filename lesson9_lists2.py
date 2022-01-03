
#         0       1       2       3       4
cars = ['bmw', 'audi', 'fiat', 'mers', 'lada']
for car in cars:
    print(car.upper())

raid1 = list(range(0, 10))
print(raid1)

for x in raid1:
    print(x)

raid1.sort(reverse=True)
print(raid1)

print("Max num = " + str(max(raid1)))
print("Min num = " + str(min(raid1)))
print("Summa numbers = " + str(sum(raid1)))

print("=================================")

#         0       1       2       3       4
cars = ['bmw', 'audi', 'fiat', 'mers', 'lada', 'uaz']

mycars = cars[1:3]
print(mycars)

mycars = cars[:2]
print(mycars)

mycars = cars[-3:-1]
print(mycars)

#        0       1       2       3       4
cars = ['bmw', 'audi', 'fiat', 'mers', 'lada', 'uaz']
mycars = cars[:]
print(mycars)
cars[0] = 'ford'
print(cars)
print(mycars)
for car in cars:
    print(car.upper())
    
