countries = ['england', 'scotland', 'wales']
print(countries)
print(f"\n Lets add ireland to the end of the list")
countries.append('ireland')
print(countries)
print(f"\n Lets print the sorted list")
print(sorted(countries))
print(f"\n Lets print the list in reverse")
print(sorted(countries, reverse=True))
print(f"\n Lets add austrilia to the start of the list")
countries.insert(0, 'austrailia')
print(countries)
print(f"\n Lets sort the list")
countries.sort()
print(countries)
print(f"\n Lets remove england from the list")
removed_country = countries.pop(1)
print(f"\n We removed {removed_country.title()} from the list")
no_of_countries = len(countries)
print(f"\n No of countries in list: {no_of_countries}")
print(f"\n Lets reverse the list")
countries.reverse()
print(countries)
print(f"\n Lets delete the list of countries")
countries.remove('wales')
countries.reverse()
print(countries)
