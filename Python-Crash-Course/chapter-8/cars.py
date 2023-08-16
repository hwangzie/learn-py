def cars(manuf, model, **car_info):
    """making a car """
    car_info['manufacturer'] = manuf
    car_info['car_mode'] = model
    return car_info

mobil = cars('subaru', 'outback', color='blue', tow_package=True)
print(mobil)
tracor = cars('ford', 'f-150', color='red', tow_package=True)
print(tracor)