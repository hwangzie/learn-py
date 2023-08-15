my_foods = ['pizza', 'falafel', 'carrot cake']

print("My favorite foods are:")
for food in my_foods:
    print(food)

friend_foods = my_foods[:]
friend_foods.append('cannoli')

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)