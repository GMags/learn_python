file = 'programming_poll.txt'

responses = []

while True:
    resp = input("Why do you like programming: ")
    responses.append(resp)
    if resp == 'quit':
        break

    with open(file, 'a') as f:
        for resp in responses:
            f.write(f"{resp.title()}\n")