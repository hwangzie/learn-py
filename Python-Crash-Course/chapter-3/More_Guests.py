my_guest = ['vahri', 'gusti', 'restu']

print(f'hi {my_guest}, i found a bigger table')

my_guest.insert(0, 'fardhu')
my_guest.insert(2, 'rei')
my_guest.append('bagas')

message = 'i would like to invite you to dinner, '
print(f'{message}{my_guest[0].title()}')
print(f'{message}{my_guest[1].title()}')
print(f'{message}{my_guest[2].title()}')
print(f'{message}{my_guest[3].title()}')
print(f'{message}{my_guest[4].title()}')
print(f'{message}{my_guest[5].title()}')
