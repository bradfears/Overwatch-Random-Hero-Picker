# Python code to pick a random Overwatch hero from a text file
import random

# Open the file in read mode
with open("heroes.txt", "r") as file:
	allText = file.read()
	words = list(map(str, allText.split()))

	# print random hero
	print(random.choice(words))
