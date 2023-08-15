pizzas = ['california', 'hawaian', 'paperoni']
friend_pizzas = pizzas[:]
pizzas.append('margherita')
friend_pizzas.append('mushroom')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
    