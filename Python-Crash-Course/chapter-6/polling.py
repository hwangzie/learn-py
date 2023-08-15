fav_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
    'james': ['c#', 'java'],
    'john': ['c++', 'c'],
}

notyet = ['james', 'john', 'jane', 'doe', 'joe']

for name in notyet:
    if name in fav_languages:
        print(f'{name.title()}, thank you for taking the poll.')
    else:
        print(f'{name.title()}, please take our poll!')
        