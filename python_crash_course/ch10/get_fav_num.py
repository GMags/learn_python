import json

filename = 'fav_num.json'


def get_fav_num():
    try:
        with open(filename, 'r', encoding='utf8') as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        pass
    else:
        print(f"Your favourite number is: {fav_num}")

get_fav_num()