# A simple dictionary
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

# Accessing values in a dictionary
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# Adding new key-value pairs
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an empty dictionary
alien_0 = {}

alien_0['color'] = 'red'
alien_0['points'] = 15

print(alien_0)

# Modifying values in a dictionary
alien_0 = {'color': 'yellow'}
print("The alien is " + alien_0['color'] + ".")
alien_0 = {'color': 'pink'}
print("The alien just became " + alien_0['color'] + ".")

# Removing key-value pairs
alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']
print(alien_0)
