guests = ['steven gerrard', 'jamie carragher', 'robbie fowler', 'Sadio Mane']

print(f"You are invited to dinner: {guests[0].title()}")
print(f"You are invited to dinner: {guests[1].title()}")
print(f"You are invited to dinner: {guests[2].title()}")
print(f"You are invited to dinner: {guests[3].title()}")

removed_guest = guests.pop(2)
print(f"\nSadly {removed_guest.title()} is unable to attend dinner")

guests.insert(2, 'roberto firmino')

print(f"\nYou are invited to dinner: {guests[0].title()}")
print(f"You are invited to dinner: {guests[1].title()}")
print(f"You are invited to dinner: {guests[2].title()}")
print(f"You are invited to dinner: {guests[3].title()}")

print(f"\nThree more players can be invited for dinner")

guests.insert(0, 'james milner')
guests.insert(4, 'jordan henderson')
guests.append('jurgen klopp')

print(f"\nYou are invited to dinner: {guests[0].title()}")
print(f"You are invited to dinner: {guests[1].title()}")
print(f"You are invited to dinner: {guests[2].title()}")
print(f"You are invited to dinner: {guests[3].title()}")
print(f"You are invited to dinner: {guests[4].title()}")
print(f"You are invited to dinner: {guests[5].title()}")
print(f"You are invited to dinner: {guests[6].title()}")

print(f"\nSorry we only have room for two people for dinner")
removed_guest = guests.pop(6)
print(f"\nSadly {removed_guest.title()} is no longer invited for dinner")
removed_guest = guests.pop(5)
print(f"\nSadly {removed_guest.title()} is no longer invited for dinner")
removed_guest = guests.pop(4)
print(f"\nSadly {removed_guest.title()} is no longer invited for dinner")
removed_guest = guests.pop(3)
print(f"\nSadly {removed_guest.title()} is no longer invited for dinner")
removed_guest = guests.pop(2)
print(f"\nSadly {removed_guest.title()} is no longer invited for dinner")

print(f"\nYou are still invited to dinner: {guests[0].title()}")
print(f"You are still invited to dinner: {guests[1].title()}")

del guests[1]
del guests[0]

print(f"\nGuest list is: {guests}")