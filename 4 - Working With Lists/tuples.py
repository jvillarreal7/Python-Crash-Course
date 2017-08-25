# Defining a tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping through all the values in a tuple
dimensions = (150, 70)
for dimension in dimensions:
	print(dimension)
	
# Writing over a tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
	print(dimension)
