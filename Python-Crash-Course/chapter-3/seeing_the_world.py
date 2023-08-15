place = ['bali', 'london', 'new york', 'paris', 'palestine']
print(place)

print(sorted(place))

print(f'{place} its still like the original list')

print(sorted(place, reverse=True))

print(f'{place} its still like the original list')

place.reverse()
print(place)
place.reverse()
print(place)

place.sort()
print(place)
place.sort(reverse=True)
print(place)
