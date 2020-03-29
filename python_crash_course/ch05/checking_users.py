current_users = ['admin', 'gerry', 'Sharon', 'ellie', 'alfie']
new_users = ['gerry', 'SHARON', 'joan', 'gerard', 'amie', 'roberta']

users_lowered = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in users_lowered:
        print(f"You will need to enter a new username")
    else:
        print(f"{new_user} is a vaild username")