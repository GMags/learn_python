filenames = ['cats.txt', 'dogs.txt']


def read_file(file):
    try:
        with open(file, encoding='utf8') as f:
            contents = f.read()

    except FileNotFoundError:
        print(f"Sorry unable to locate {file} ")
    else:
        print(f"\nThe {file} contains:")
        print(contents)


for file in filenames:
    read_file(file)