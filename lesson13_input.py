#=================
#=================Form of authentification==================




while True:
    name = input("Input your name: ")
    print("Your name: " + name)
    password = input("Enter your password: ")
    if password == '1988' and name == 'Ivan':
        print("Hello, " + name)
        break
    else:
        print("Your name and password are false!")

#============Input list from users===============

mylist = []
msg = ""

while msg != "stop".title():
    msg = input("Enter new name and Stop to finish ")
    mylist.append(msg)

for Name in mylist:
    print(Name)
    
