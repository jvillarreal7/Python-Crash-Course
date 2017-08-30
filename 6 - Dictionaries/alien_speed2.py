# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# Iterate and replace aliens
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
		print(alien)
	
# Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))
