# ordinal_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

ordinal_num = list(range(1, 10))

for num in ordinal_num:
    if num == '1':
        print(f"The number is {num}st")
    elif num == '2':
        print(f"\nThe number is {num}nd")
    elif num == '3':
        print(f"\nThe number is {num}rd")
    else:
        print(f"\nThe number is {num}th")