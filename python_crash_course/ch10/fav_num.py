import json

filename = 'fav_num.json'


def get_fav_num():
    fav_num = input("Please enter your favourite number: ")
    with open(filename, 'w', encoding='utf8') as f:
        json.dump(fav_num, f)
    return fav_num

get_fav_num()



