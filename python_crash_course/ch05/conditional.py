car = 'Rover'

if car == 'Rover':
    print("I predict true")
    print(f"\ncar is a {car}")

if car == 'Sabb':
    print('I predict false')
    print(f"\n car is {car}")


cars = ['BMW', 'VW', 'Seat', 'Vauxhall', 'ford', 'peugeot']

mycar = 'audi'
sharon_car = 'vauxhall'

if mycar not in cars:
    print(f"\nMy {mycar} is not listed in the car index.")

for car in cars:
    car = car.lower()
    if sharon_car == car:
        print(f"\nSharons {sharon_car} belongs to the car index.")


myage = 35

if myage > 18:
    print(f"\nYour are old enough to drink:")

if myage <= 40:
    print(f"\nCongrats you are under 40")