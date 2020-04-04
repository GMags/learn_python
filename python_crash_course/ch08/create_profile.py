import user_profile as up

user_profile = up.build_profile(
    'albert',
    'einstein',
    location='princeton',
    field='physics'
)

my_profile = up.build_profile(
    'gerry',
    'maguire',
    age=35,
    date_of_birth='30/01/1985',
    occupation='devops engineer'
)

ellie_profile = up.build_profile(
    'ellie',
    'maguire',
    age=14,
    gendor='femaile',
    date_of_birth='30/05/2005'
)

print(user_profile)
print("\n")
print(my_profile)
print("\n")
print(ellie_profile)
print("\n")

ellie_age = ellie_profile['age']
print(f"Ellie's age is: {ellie_age}")