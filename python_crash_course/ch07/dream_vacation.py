name_prompt = f"Please enter your name "
place_prompt = f"\nIf you could visit one place in the world, where would you go? "
quit_prompt = f"\nWould you like to continue? Y/N ?"

resp = {}

poll = True
while poll:
    name = input(name_prompt)
    place = input(place_prompt)

    resp[name] = place

    repeat = input(quit_prompt)
    if repeat == 'N':
        poll = False

print(f"\n----- RESULTS -------")
for name, place in resp.items():
    print(f"{name.title()} would like to go to {place.title()}")

