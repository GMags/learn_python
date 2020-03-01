pizzas = ['magherita', 'pepperoni', 'pineapple and ham', 'BBQ chicken']

for pizza in pizzas:
    print(pizza)

print(f"\n")

for pizza in pizzas:
    print(f"I like {pizza} pizza\n")

print(f"I really love pizza!")

new_pizzas = pizzas[:]
new_pizzas.insert(0, 'sizzler')

print(f"\n")

print(f"The first 3 new pizzas are:")
for pizza in new_pizzas[:3]:
    print(pizza.title())

print(f"\n")

print(f"The items in the middle of the list are:")
for pizza in new_pizzas[2:4]:
    print(pizza.title())

print(f"\n")

print(f"The last 3 items of the list are:")
for pizza in new_pizzas[2:]:
    print(pizza.title())

pizzas.append('Tuna and sweetcorn')

print(f"\n")

print(f"My favorite pizzas are:")
for mypizza in pizzas:
    print(mypizza.title())

print(f"\nMy friend’s favorite pizzas are:")
for friends_pizza in new_pizzas:
    print(friends_pizza.title())

