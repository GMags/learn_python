prompt = "\nPlease enter your age: "
prompt += "\nType quit to finish: "

while True:
    resp = input(prompt)
    if resp == "quit":
        break

    age = int(resp)

    if age < 3:
        print(f"Congrats you can see the movie for free!")
    elif age < 13:
        print(f"The ticket cost is £10")
    else:
        print(f"The ticket cost is £15")