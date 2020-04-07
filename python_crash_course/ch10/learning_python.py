file = 'learning_python.txt'

print("1st --- Print of file ")
with open(file) as f:
    contents = f.read()
    print(contents)

print("2nd --- Print of file ")
with open(file) as f:
    for line in f:
        print(line.rstrip())

print("3rd --- Print of file ")
with open(file) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())
