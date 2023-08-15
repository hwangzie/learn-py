someone_1 = {
    'first_name' : 'zaim',
    'last_name' : 'shidqi',
    'age' : 19,
    'city' : 'jakarta',

}

someone_2 = {
    'first_name' : 'hwang',
    'last_name' : 'hyunjin',
    'age' : 20,
    'city' : 'seoul',
}

someone_3 = {
    'first_name' : 'kim',
    'last_name' : 'seungmin',
    'age' : 20,
    'city' : 'seoul',
}

people = [someone_1, someone_2, someone_3]

for person in people:
    print(f'\n{person["first_name"]} {person["last_name"]} from {person["city"]}')
