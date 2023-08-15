cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes',
    },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby mountains': 'alaska range',
    },
    'pontianak': {
        'country': 'indonesia',
        'population': 573_751,
        'nearby mountains': 'meratus',
    },
}

for city, city_info in cities.items():
    region = city_info['country']

    print(city + f' is from {region} and have a nearby montain {city_info["nearby mountains"]}')
    print(f"and the population is around {city_info['population']}")
