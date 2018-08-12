#!/usr/loca/env python3.6

xmen_file = open('xmen_base.txt', 'r')

for line in xmen_file:
    print(line, end="") 

xmen_file.close()   

xmen_base = open('xmen_base.txt')
new_xmen = open('new_xmen.txt', 'w')

new_xmen.write(xmen_base.read())
new_xmen.close()
new_xmen = open(new_xmen.name, 'r+')
new_xmen.read()
new_xmen.seek(10)
new_xmen.write("TEST")

for line in new_xmen:
    print(line, end="")

new_xmen.close()

with open('xmen_base.txt', 'a') as file:
    file.write('Professor Xavier\n')

file = open('xmen_base.txt', 'a')
with file:
    file.write("I want to be an Xman\n")