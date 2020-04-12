
def get_city_info(country, city, population=0):
    """Function to return city string of city and county"""

    if population:
        formated_city = f"{country}, {city}, {population}"
    else:
        formated_city = f"{country}, {city}"
    return formated_city.title()


get_city_info('ireland', 'dublin', '10000000')

get_city_info('england', 'london')