def city_country(city, country):
    msg = f"{city.title()}, {country.title()}"
    return msg


city = city_country('madrid', 'spain')
print(city)
city = city_country('belfast', 'ireland')
print(city)
city = city_country('rome', 'italy')
print(city)