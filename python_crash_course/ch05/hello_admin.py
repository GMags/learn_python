users = []

if users:
    for user in users:
        if user == 'admin':
            print(f"\nHello {user}, would you like to see status report")
        else:
            print(f"\nHello {user}, thank you for logging in again!")
else:
    print(f"We need to find some users")