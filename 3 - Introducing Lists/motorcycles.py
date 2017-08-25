# Create list with elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Append elements to existing list
motorcycles.append('ducati')
print(motorcycles)

# Append elements to an empty list
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Insert elements into a list
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Delete elements from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles)

# Pop element from a list
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop(0)
print("The last motorcycle I owned was a %s" % (last_owned.title()))

# Removing item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA %s is too expensive for me!" % (too_expensive.title()))

