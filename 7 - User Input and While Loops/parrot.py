# How the input() function works
message = input("Tell me something and I'll repeat it back to you: ")
print(message)

# While loop: letting the user choose when to quit
prompt = "\nTell me something and I'll repeat it back to you: \n"
prompt += "\nEnter 'quit' to end the program. "
active = True

while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print(message)
