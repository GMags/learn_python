# fav_numbers = {
#     'gerry': 23,
#     'sharon': 5,
#     'ellie': 30,
#     'joan': 42,
#     'amie': 18,
#     'gerard': 4,
#     }
#
# num = fav_numbers['gerry']
# print(f"Gerry favourite number is: {num}")
# num = fav_numbers['sharon']
# print(f"\nSharon favourite number is: {num}")
# num = fav_numbers['ellie']
# print(f"\nEllie favourite number is: {num}")
# num = fav_numbers['joan']
# print(f"\nJoan favourite number is: {num}")
# num = fav_numbers['amie']
# print(f"\nAmie favourite number is: {num}")
# num = fav_numbers['gerard']
# print(f"\nGerard favourite number is: {num}")

fav_numbers = {
    'gerry': [23, 30],
    'sharon': [5, 23, 30],
    'ellie': [30, 18],
    'joan': [42, 18, 5, 30, 23],
    'amie': [18, 17, 92],
    'gerard': [4, 5, 6]
    }

for name, numbers in fav_numbers.items():
    print(f"\n{name.title()} like the below numbers:")
    for num in numbers:
        print(f"{num}")
