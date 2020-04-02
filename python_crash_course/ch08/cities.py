def describe_city(name, country='ireland'):
    print(f"\n{name.title()} is located in {country.title()}")


describe_city('belfast')
describe_city(name='dublin')
describe_city('madrid', 'spain')