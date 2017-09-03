prompt = "\nPlease enter the name of a city you've visited ('quit' to finish): "

while True:
	city = input(prompt)
	
	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")
