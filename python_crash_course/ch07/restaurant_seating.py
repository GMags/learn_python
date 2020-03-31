party = input("How many people are in your dinner group? ")
party = int(party)

if party > 8:
    print(f"Im sorry you will have to wait for an available table.")
else:
    print(f"Please follow me your table is ready!")