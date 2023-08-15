age = 80
# if age < 4:
#     print("Your admission cost is $0.")
# elif age < 18:
#     print("Your admission cost is $5.")
# else:
#     print("Your admission cost is $10.")

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print(f'your admission cost is ${price}')

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65: # this is the same as else if
    price = 10
elif age >= 65:
    price = 5

print(f'your admission cost is ${price}')


