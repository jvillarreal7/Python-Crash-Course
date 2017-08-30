# A list in a dictionary
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}

print("You ordered a " + pizza['crust'] + "-crust pizza " +
	"with the followong toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)
