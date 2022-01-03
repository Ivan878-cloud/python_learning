# =================Условные операторы==========================

x = 26

if x == 25:
    print("Yes, you are right!!!")
else:
    print("No, you are wrong!!!\n\n\n\n")

# ===================NEXT TASK================

age = 2
if age <=4:
    print("You are baby!")
elif age > 4 and age < 12:
    print("You are kind!")

elif age >= 12 and age < 19:
    print("You are tenager!!!")
else:
    print("You are old man")

print("------------THE END!!!")

# =================NEXT TASK========================

print("\n\n\n\nnext task\n\n\n\n")

cars = ['bmw', 'audi', 'fiat', 'mers', 'lada', 'uaz']
RUS_AUTO = ['lada', 'uaz']

if 'lada' in cars:
    print("Yes, lada is in the raid")
else:
    print("No, lada isn't in the raid")

for car in cars:
    if car in RUS_AUTO:
        print(car + " made in Russia!")
    else:
        print(car + " made not in Russia:(((")
        