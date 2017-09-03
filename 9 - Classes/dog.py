class Dog():
	# Simple attempt to model a dog.

	def __init__(self, name, age):
		# Initialize name and age attributes.
		self.name = name
		self.age = age

	def sit(self):
		# Simulate a dog sitting in response to a command.
		print("{} is now sitting.".format(self.name.title()))

	def roll_over(self):
		# Simulate a dog rolling over in response to a command.
		print("{} rolled over!".format(self.name.title()))

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print("My dog's name is {}.".format(my_dog.name.title()))
print("My dog is {} years old.".format(my_dog.age))

my_dog.sit()

print("Your dog's name is {}.".format(your_dog.name.title()))
print("Your dog is {} years old.".format(your_dog.age))

your_dog.roll_over()
