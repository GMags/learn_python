def build_profile(first, last, **user_info):
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()

    return user_info


user_profile = build_profile(
    'albert',
    'einstein',
    location='princeton',
    field='physics'
)

my_profile = build_profile(
    'gerry',
    'maguire',
    age=35,
    date_of_birth='30/01/1985',
    occupation='devops engineer'
)

print(user_profile)
print("\n")
print(my_profile)