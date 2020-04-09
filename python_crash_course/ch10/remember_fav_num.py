import json

filename = 'fav_num.json'


def fav_num():
    try:
        with open(filename, 'r', encoding='utf8') as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        fav_num = input("Please enter your favourite number: ")
        with open(filename, 'w', encoding='utf8') as f:
            json.dump(fav_num, f)
    else:
        print(f"Your favnumber is {fav_num}")


fav_num()
