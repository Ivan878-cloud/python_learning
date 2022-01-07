

input_file1 = "surname.txt"
outputfile = "select_file.txt"
myfile1 = open(input_file1, mode='r', encoding='utf_8')
myfile3 = open(outputfile, mode='a', encoding='utf_8')


#================INPUT=============================

a = input("Please, enter simbol: ")
b= input("Please, enter simbol: ")



for num, line in enumerate(myfile1):
    if a in line:
        myfile3.write("Found surname: " + str(num) + " " + line.strip() + "\n")


input_file2 = "numbers_phone.txt"

myfile2 = open(input_file2, mode='r', encoding='utf_8')

for num, line in enumerate(myfile2):
    if b in line:
        myfile3.write("Found number: " + str(num) + " " + line.strip() + "\n")


myfile3 = open(outputfile, mode='r', encoding='utf_8')

for num, line in enumerate(myfile3):
    print(str(num) + " " + line.strip() + " ")

