my_guest = ['vahri', 'gusti', 'restu']

cant_come = my_guest.pop(1)
print(cant_come.title() + " can't come to my dinner")

my_guest.insert(1, 'fardhu')
message = 'i would like to invite you to my dinner, '

print(message + my_guest[0].title())
print(message + my_guest[1].title())
print(message + my_guest[2].title())
