#!/usr/bin/python3.6

message = input("Please enter a message: " )
count = input("Please enter the number of repeats, default is 1: ").strip()

if count:
    count = int(count)
else:
    count = 1

def echo(message, count):
    while count > 0:
        print(message)
        count -= 1

echo(message, count)