favorite_places = {
    'sharon': ['majorca', 'las vegas', 'portugal'],
    'gerry': ['las vegas', 'florida', 'majorca'],
    'ellie': ['florida', 'majorca', 'turkey']
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes to visit:")
    for place in places:
        print(f"{place.title()}")

