def show_messages(messages):
    print('----Show Messages----')
    for message in messages:
        print(message.title())

def send_messages(messages, sent_messages):
    print('\n----Send Messages----')

    while messages:
        msg = messages.pop()
        print(f"{msg.title()}")
        sent_messages.append(msg)


messages = ['i love python', 'we won it six times', 'nobody like covid-19']
sent_messages = []
show_messages(messages)
send_messages(messages, sent_messages)

print("\n----Lists-----")
print(messages)
print(sent_messages)
