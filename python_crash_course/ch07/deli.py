sandwich_orders = ['chicken tikka', 'blt', 'cheese and ham', 'tuna', 'salad', 'ham']

finished_sandwiches = []

# while sandwich_orders:
#     for sandwich in sandwich_orders:
#         print(f"I have made your {sandwich.title()} sandwich")
#
#         finished_sandwiches.append(sandwich)
#         sandwich_orders.remove(sandwich)

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I have made your {sandwich.title()} sandwich")
    finished_sandwiches.append(sandwich)


print(f"\nThe following sandwiches have been made:")
for completed_sandwich in finished_sandwiches:
    print(completed_sandwich.title())