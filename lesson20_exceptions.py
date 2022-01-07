
import sys

f_name = "surnam.txt"


while True:
    try:
        print("inside try")
        myfile = open(f_name, mode='r', encoding='utf=8')
    except Exception:
        print("inside EXCEPT")
        print("Error found!")
        print(sys.exc_info()[1])
        f_name = input("Enter correct filename or directory: ")
    else:
        print("inside ELSE")
        print(myfile.read())
        break


print("=======================EOF=========================")