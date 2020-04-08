print(f"Enter two numbers and i will add them:")
print(f"Press 'q' to quit!")

while True:
    try:
        first_num = input(f"\nPlease enter the first number ")
        if first_num == 'q':
            break

        second_num = input(f"\nPlease enter the second number ")
        if second_num == 'q':
            break

        int(first_num)
        int(second_num)

    except ValueError:
        print(f"Sorry the value entered is not a number:")
    else:
        answer = first_num + second_num
        print(f"The answer is: {answer}")

