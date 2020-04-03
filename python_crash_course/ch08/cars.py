def make_car(manufacturer, model, **extras):

    car_info = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
    }

    for extra, val in extras.items():
        car_info[extra] = val

    return car_info


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

my_car = make_car('audi', 'a4', color='white', navigaton='sat-nav', sensors='parking-sensors', interior='heated seats')
print(my_car)