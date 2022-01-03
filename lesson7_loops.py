#===========Циклы===========


for x in range(0,10, 2):
    print("number x = " + str(x))
    print("__________")
    if x == 6:
        break

x = 18
while True:
    print(x)
    x = x - 1
    if x == 10:
        break