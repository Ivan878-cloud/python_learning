#===========function_raids_and_dictionaries==========

def tel_notes(name, telephone, address):
    """tel_notes"""
    note = {
        'name': name,
        'telephone': telephone,
        'address': address
    }
    return note

user1 = tel_notes("Ivan", "+79152381882", "Krasnogorsk")
user2 = tel_notes("Jan", "+79127005227", "Kirov")

print(user1)
print(user2)

def give_dolzh(masters, *persons):
    """give_dolzhnost"""
    for person in persons:
        print("Mehan " + person.upper() + " recieve dolzhnost " + masters)

give_dolzh("PD", "Ivanov", "Petrov")
give_dolzh("PDS", "Sidorov")
