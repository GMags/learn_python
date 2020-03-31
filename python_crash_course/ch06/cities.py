cites = {
    'las vegas': {
        'country': 'usa',
        'population': 30000,
        'fact': 'Las Vegas is in the nevada dessert'
         },

    'belfast': {
        'country': 'ireland',
        'population': 10000,
        'fact': 'cme group has an office in Belfast'
        },

    'london': {
        'country': 'england',
        'population': 1000000,
        'fact': 'Big Ben is in London'
        }
}

# for city, city_info in cites.items():
#     print(f"\n{city.title()} has the following info:")
#     for k, v in city_info.items():
#         print(f"{k.title()} = {v}")

for city, city_info in cites.items():
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(f"\n{city.title()} is located in {country.title()}")
    print(f"It currectly has a population of {float(population)}")
    print(fact)

