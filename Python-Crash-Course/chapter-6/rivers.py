rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states',
    'yangtze': 'china',
    'kapuas': 'indonesia',
    'mekong': 'vietnam',
}

for items in rivers:
    print(f'The {items.title()} runs through {rivers[items].title()}')