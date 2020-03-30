pets = []

pet = {
    'kind': 'dog',
    'breed': 'cavapoo',
    'name': 'alfie',
    'owner': 'gerry',
    'colour': 'brown',
}

pets.append(pet)

pet = {
    'kind': 'dog',
    'breed': 'lababour',
    'name': 'bailey',
    'owner': 'ellie',
    'colour': 'black',
    }

pets.append(pet)

pet = {
    'kind': 'snake',
    'breed': 'python',
    'name': 'sneek',
    'owner': 'sharon',
    'colour': 'green',
    }

pets.append(pet)

for pet in pets:
    print(f"\nHere is the animal details for: {pet['name'].title()}")
    for k, v in pet.items():
        print(f"{k.title()} - {v.title()}")
