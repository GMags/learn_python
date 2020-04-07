from random import choice

pool = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')

winning_numbers = []

#my_ticket = (5, 7, 'a', 'e')

attempts = 0
won = False
max_attempts = 1_000

print("Tonights winning lottery numbers are:")
print("")


def create_ticket(pool):
    my_ticket = []

    while len(my_ticket) < 4:
        num = choice(pool)

        if num not in my_ticket:
            my_ticket.append(num)

    return my_ticket

def lottery_draw():
    """Define the lottery draw of 4 numbers"""

    while len(winning_numbers) < 4:

        num = choice(pool)

        if num not in winning_numbers:
            print(f"-- Ball drawn is {num}")
            winning_numbers.append(num)

    return winning_numbers


def check_ticket(my_ticket, winning_numbers):
    """Check if my lottery ticket matches the winning lottery numbers"""

    for num in my_ticket:
        if num not in winning_numbers:
            return False

    return True

lottery_draw()
print(f"\nLottery Result is:")
print(winning_numbers)

while not won:
    ticket = create_ticket(pool)
    won = check_ticket(ticket, winning_numbers)
    attempts += 1
    if attempts >= max_attempts:
        break

if won:
    print(f"\nMy ticket: {ticket}")
    print(f"Congratulations!!!!!!!!!!!")
    print(f"It took {attempts}")
else:
    print(f"Sorry to matching numbers in {attempts} attempts")
    print(f"My ticket: {ticket}")
    print(f"Winning numbers: {winning_numbers}")


