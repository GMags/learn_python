users = []

gerry = {
    'first_name': 'Gerry',
    'last_name': 'maguire',
    'age': 35,
    'city': 'cookstown',
    }

users.append(gerry)

sharon = {
    'first_name': 'sharon',
    'last_name': 'maguire',
    'age': 39,
    'city': 'cookstown',
    }

users.append(sharon)

ellie = {
    'first_name': 'ellie',
    'last_name': 'maguire',
    'age': 13,
    'city': 'cookstown',
    }

users.append(ellie)

for user in users:
    print("\nEach user has the following details:")
    print(user['first_name'].title(), user['last_name'].title())
    print(user['age'])
    print(user['city'].title())



# print(f"My first name is: {person_info['first_name'].title()}")
# print(f"\nMy last name is: {person_info['last_name'].title()}")
# print(f"\nMy age is: {person_info['age']}")
# print(f"\nI live in: {person_info['city'].title()}")
