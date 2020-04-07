file = 'guest.txt'

guest = input("Please enter your name: ")

with open(file, 'w') as f:
    f.write(guest)