sandwich_orders = ['chicken tikka', 'blt', 'cheese and ham', 'pastrami', 'salad', 'ham', 'pastrami', 'pastrami']
finished_sandwiches = []

print(f"Sorry the deli has ran out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    sandwich_orders.remove(sandwich)

print(f"\nThe following sandwiches have been made:")
for completed_sandwich in finished_sandwiches:
    print(completed_sandwich.title())