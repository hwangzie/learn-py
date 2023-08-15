# bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# print(bicycles)

# print(bicycles[0])

# print(bicycles[0].title())

# message = f"My frist biycle was a {bicycles[2].title()}."

# print(message)

# motorcycles = ['honda', 'yamaha', 'suzuki']

# print(motorcycles)

# motorcycles[0] = 'bmw'

# print(motorcycles)

# motorcycles.append('ducati')

# print(motorcycles)

cars = []
#memasukkan value dari depan
cars.append('toyota')
cars.append('daihatsu')
cars.append('subaru')

# print(cars)
#inserting / memasukkan value dengan tempat yang spesifik 
cars.insert(0, 'volkswagen')

# print(cars)
# #mengahapus list urutan ke 1/ indeks ke 0
# del cars[0]

# print(cars)

# popped_cars = cars.pop()#menyimpan value yang di pop
# print(cars)
# print(popped_cars)

# last_owned = popped_cars
# print(f'The last car i owned was a {last_owned.title()}')

# cars.remove('daihatsu')
# print(cars)

print(cars)

too_expensive = 'volkswagen'
cars.remove(too_expensive)

print(cars)
print(f'{too_expensive.title()} is too expensive to me.')