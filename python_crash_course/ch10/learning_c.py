file = 'learning_python.txt'

with open(file) as f:
    contents = f.readlines()

for line in contents:
    print(line.replace('Python', 'C').strip())
