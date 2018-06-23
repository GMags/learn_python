#!/usr/bin/env python3.6

user = {'admin' : False, 'active' : True, 'name': 'Gerry'}

if user['admin'] and user['active']:
    print(f"ACTIVE - (ADMIN) = " + user['name'])
elif user['admin']:
    print(f"(ADMIN) = " + user['name'])
elif user['active']:
    print(f"ACTIVE - " + user['name'])
else:
    print(user['name'])