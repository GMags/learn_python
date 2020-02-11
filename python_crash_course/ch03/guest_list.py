guests = ['steven gerrard', 'jamie carragher', 'robbie fowler', 'Sadio Mane']

print(f"You are invided to dinner: {guests[0].title()}")
print(f"You are invided to dinner: {guests[1].title()}")
print(f"You are invided to dinner: {guests[2].title()}")
print(f"You are invided to dinner: {guests[3].title()}")

removed_guest = guests.pop(2)
print(f"\nSadly {removed_guest.title()} is unable to attend dinner")

guests.insert(2, 'roberto firmino')

print(f"\nYou are invided to dinner: {guests[0].title()}")
print(f"You are invided to dinner: {guests[1].title()}")
print(f"You are invided to dinner: {guests[2].title()}")
print(f"You are invided to dinner: {guests[3].title()}")

print(f"\n Three more players can be invited for dinner")

guests.insert(0, 'james milner')
guests.insert(4, 'jordan henderson')
guests.append('jurgen klopp')

print(f"\nYou are invided to dinner: {guests[0].title()}")
print(f"You are invided to dinner: {guests[1].title()}")
print(f"You are invided to dinner: {guests[2].title()}")
print(f"You are invided to dinner: {guests[3].title()}")
print(f"You are invided to dinner: {guests[4].title()}")
print(f"You are invided to dinner: {guests[5].title()}")
print(f"You are invided to dinner: {guests[6].title()}")
