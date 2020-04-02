def make_shirt(size='L', message='i love python'):
    print(f"\nThe size of the t-shirt is: {size}")
    print(f"\nThe t-shirt has the message: {message.title()}")


make_shirt()
make_shirt(size='M')
make_shirt(size='XL', message='i love rust')
