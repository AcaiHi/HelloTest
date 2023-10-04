import math


HOT_DOGS_PER_PACKAGE = 10
HOT_DOGS_BUNS_PER_PACKAGE = 8

attendees = int(input('Enter the number of guests: '))

hot_dogs_per_person = int(input('Hot dogs per person: '))


required_hot_dogs = attendees * hot_dogs_per_person
packages_of_hot_dogs = required_hot_dogs / HOT_DOGS_PER_PACKAGE
packages_of_hot_dog_buns = required_hot_dogs / HOT_DOGS_BUNS_PER_PACKAGE

print(f"You require {math.ceil(packages_of_hot_dogs)} packs of hot dogs for the cookout.")
print(f"You require {math.ceil(packages_of_hot_dog_buns)} packs of buns for the cookout.")

remain_hotdogs = (math.ceil(packages_of_hot_dogs) * HOT_DOGS_PER_PACKAGE) - required_hot_dogs
if remain_hotdogs != 0:
    print(f'You have {remain_hotdogs} left over hot dogs')

remain_buns = (math.ceil(packages_of_hot_dog_buns) * HOT_DOGS_BUNS_PER_PACKAGE) - required_hot_dogs
if remain_buns != 0:
    print(f'You have {remain_buns} left over hot dog buns. ')