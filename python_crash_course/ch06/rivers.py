rivers = {
    'nile': 'egypt',
    'liffey': 'ireland',
    'amazon': 'brazil'
    }

for river, country in rivers.items():
    print(f"\nThe {river.title()} runs through {country.title()}")

print(f"\nWe have the following rivers:")
for river in rivers.keys():
    print(river.title())

print(f"\nWe have the following countries:")
for country in rivers.values():
    print(country.title())

