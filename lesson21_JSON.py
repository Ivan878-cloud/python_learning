#==========================================#
#==========learning JSON===================#
import json
settings = "settings_of_worker.txt"
mysettings = open(settings, mode='w', encoding='Latin-1')

worker1 = {
    'surname': "Ivanov",
    'zp': 1000,
    'awards': ["Blagodarnost", "Pochertnaya", "Premia"]
}

worker2 = {
    'surname': "Petrov",
    'zp': 1500,
    'awards': ["Premia"]
}

brigada = []
brigada.append(worker1)
brigada.append(worker2)

#==============SAVE BY JSON==============#

json.dump(brigada, mysettings)
mysettings.close()
#=============LOAD BY JSON====================#

mysettings = open(settings,mode='r', encoding='Latin-1')
json_load = json.load(mysettings)

for worker in json_load:
    print("Worker's surname is " + worker['surname'])
    print("Worker's zp  " + str(worker['zp']))
    print("Worker's awards " + str(worker['awards']))
    print("\n----------------------------------------\n")




