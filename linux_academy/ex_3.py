#!/usr/bin/env python3.6
import json

users = [ {'admin' : False, 'active' : True, 'name' : 'Gerry'},
          {'admin' : False, 'active' : True, 'name' : 'Nathan'},
          {'admin' : True, 'active' : True, 'name' : 'Sharon'},
          {'admin' : False, 'active' : False, 'name' : 'Rachel'}
]

#print(json.dumps(users, indent=1, sort_keys=True))

line = 1

for user in users:
    if user['admin'] and user['active']:
        print(f"{line} - ACTIVE - (ADMIN) = " + user['name'])
    elif user['admin']:
        print(f"{line} - (ADMIN) = " + user['name'])
    elif user['active']:
        print(f"{line} - ACTIVE - " + user['name'])
    else:
        print(f"{line} - NOT ACTIVE OR ADMIN = " + user['name'])
    line += 1