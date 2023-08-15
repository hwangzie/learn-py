requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

requested_toppings = ['mushrooms', 'onions', 'pineapple', 'extra cheese']
'mushrooms' in requested_toppings # True
'pepperoni' in requested_toppings # False

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# for req_topping in requested_toppings:
#     print(f'adding {req_topping}')

# print("\nFinished making your pizza!")

for req_topping in requested_toppings:
    if req_topping == 'pineapple':
        print(f'Sorry, we are out of {req_topping} right now.')
    else:
        print(f'Adding {req_topping}')

print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings:
    for req_topping in requested_toppings:
        print(f'Adding {req_topping}')
    print('\nFinised making your pizza!')
else :
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for req in requested_toppings:
    if req in available_toppings:
        print(f'Adding {req}.')
    else:
        print(f"Sorry, we don't have {req}.")