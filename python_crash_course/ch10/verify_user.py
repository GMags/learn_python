import json

filename = 'users.json'


def get_saved_username():

    try:
        with open(filename, 'r') as f:
          username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_username():

    username = input("Please enter your username ")
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(username, f)
    return username


def greet_user():
    username = get_saved_username()

    if username:
        verified_user = input(f"Are you the {username}? y/n")
        if verified_user == 'y':
            print(f"Welcome back {username}")
        else:
            username = get_username()
            print(f"{username} we will store this for the next time")

greet_user()