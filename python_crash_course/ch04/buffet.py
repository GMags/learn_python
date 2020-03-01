menu_items = ('chips', 'cheese burger', 'soup', 'cheese & ham toastie', 'chichen salad')

print(f"The items on the menu are:")

for items in menu_items:
    print(f" - {items.title()}")

menu_items = (
    'chips', 'cheese burger', 'soup', 'cheese & ham toastie', 'chichen salad', 'steak', 'peppered checken'
    )

print(f"\nThe new items on the menu are:")

for items in menu_items:
    print(f" - {items.title()}")