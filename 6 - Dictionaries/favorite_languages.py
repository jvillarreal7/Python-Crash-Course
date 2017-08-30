# Dictionary of similar objects
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
	}

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
	 language.title() + ".")

# Looping through all the keys
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print("\tHi " + name.title() +
			", I see your favorite language is " +
			favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!\n")

# Looping through a dictionary's keys in order
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking our poll!")

# Looping through all the values
print("\nThe following languages were mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

# List inside a dictionary
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell']
	}

for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())
