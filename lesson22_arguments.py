
import sys
import os


a = len(sys.argv)

if a < 1:
    print("Arguments no provided!!!")
else:
    print("Arguments entered!!!" + str(sys.argv[1:]))

os.system("vim surname.txt")
os.