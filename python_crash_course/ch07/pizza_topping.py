prompt = "\nPlease enter a pizza topping: "
prompt += "\nType quit to finish: "

while True:
    resp = input(prompt)
    if resp != "quit":
        print(f"We will add {resp} to the pizza topping")
    else:
        break
