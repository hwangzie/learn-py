dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250 # TypeError: 'tuple' object does not support item assignment

# Looping Through All Values in a Tuple
for dimension in dimensions:
    print(dimension)

print('original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)


