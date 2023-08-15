pet_0 = {
    'name' : 'buddy',
    'type' : 'dog',
    'owner' : 'john',
}

pet_1 = {
    'name' : 'lucy',
    'type' : 'cat',
    'owner' : 'jane',
}

pet_2 = {
    'name' : 'billy',
    'type' : 'bird',
    'owner' : 'doe',
}

pets = [pet_0,pet_1,pet_2]

for pet in pets:
    print(f"{pet['name']} is a {pet['type']} and the owner is {pet['owner']}")