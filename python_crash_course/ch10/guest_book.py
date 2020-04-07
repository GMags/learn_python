file = 'guest_book.txt'

while True:
    name = input("Please enter your name: ")
    if name == 'quit':
        break
    print(f"Welcome {name.title()}")

    with open(file, 'a') as f:
        record = f"User {name.title()} visted:\n"
        f.write(record)

