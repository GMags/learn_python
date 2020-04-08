filenames = ['a_tale_of_two_cites.txt', 'little_women.txt', 'the_call_of_the_wild.txt']


# def count_words(file):
#     try:
#         with open(file, encoding='utf8') as f:
#             contents = f.read()
#     except FileNotFoundError:
#         print(f"Unable to open file {file}")
#     else:
#         found = contents.lower().count('the ')
#     print(f"\nThe book {file} contains the word 'the' aprox {found} times")

def count_words(file):
    total = 0
    try:
        with open(file, encoding='utf8') as f:
            contents = f.readlines()
    except FileNotFoundError:
        print(f"Unable to open file {file}")
    else:
        for line in contents:
            found = line.lower().count('the ')
            total += found

    print(f"\nThe book {file} contains the word 'the' aprox {total} times")


for file in filenames:
    count_words(file)
