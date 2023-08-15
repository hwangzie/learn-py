foods = ('rice', 'beans', 'chicken', 'beef', 'pork')
print("Original menu:")
for food in foods:
    print(food.title())

# foods[0] = 'rice and beans' # TypeError: 'tuple' object does not support item assignment

foods = ('rice and beans', 'chicken', 'beef', 'pork')  
print("\nNew menu:")
for food in foods:
    print(food.title())
