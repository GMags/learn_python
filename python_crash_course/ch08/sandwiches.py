def make_sandwich(bread, *fillings):
    print(f"\nWe will have a sandwich with {bread.title()} bread with the following fillings:")
    for filling in fillings:
        print(f" - {filling.title()}")

make_sandwich('while', 'cheese', 'ham')
make_sandwich('brown', 'tuna', 'sweetcorn')
make_sandwich('granery', 'cheese', 'chichen tika', 'peppers', 'onion')