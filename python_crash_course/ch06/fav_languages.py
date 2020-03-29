favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

print("\n")

users = ['sarah', 'sharon', 'gerry', 'phil', 'ellie', 'amie']

for user in users:
    if user in favorite_languages.keys():
        print(f"\nThank you {user.title()} for already taking the poll")
    else:
        print(f"\n{user.title()} what is your favourite programming language?")



