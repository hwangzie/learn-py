fav_place = {
    'james': ['japan', 'korea', 'china'],
    'john': ['indonesia', 'singapore', 'malaysia'],
    'jane': ['thailand', 'vietnam', 'laos'],
    'doe': ['philippines', 'myanmar', 'cambodia'],
}

for name, places in fav_place.items():
    print(name + "'s favorite place are:")
    for place in places:
        print(f"\t-{place}")