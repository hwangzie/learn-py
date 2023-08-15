fav_number = {
    'james': [7, 8, 9],
    'john': [3, 4, 5],
    'jane': [5, 6, 7],
    'doe': [9, 10, 11],
}

for name, number in fav_number.items():
    print(name + "'s favorite number is ")
    for numbers in number:
        print(numbers)

