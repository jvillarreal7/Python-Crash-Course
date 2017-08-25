# Using range() to make a list of squared numbers
squares = []
for value in range(1,11):
	squares.append(value**2)
	
print(squares)

# List comprehensions (same result as above, less lines)
squares = [value**2 for value in range(1,11)]
print(squares)
