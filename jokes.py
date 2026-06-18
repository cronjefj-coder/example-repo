# ********** Pseudocode **********

# The algorythm should use random generation to select a joke and its relevant punchline
# Print out the joke and the punchline

# I researched the Python documentation on random module to decide which random mode will
# be best suited for the task.
# https://docs.python.org/3/library/random.html#module-random
# I also used ChatGPT to generate 10 short jokes and their punchlines
# https://chatgpt.com/share/6a0ad199-f59c-83ea-90ba-307c21558ad5

# Import the random module
import random

# Create dictionaries for the jokes

jokes = {1:"Why don't scientists trust atoms?", 2:"Why did the scarecrow win an award?",
         3:"Why don't skeletons fight each other?", 4:"What do you call fake spaghetti?",
         5:"Why did the mathbook look sad?", 6:"What do you call cheese that isn't yours?",
         7:"Why can't your nose be 12 inches long?", 8:"What do you call a bear with no teeth?",
         9:"Why did the bicycle fall over?", 10:"What did the one wall say to the other wall?"}

punchlines = {1:"Because they make up everything.", 2:"Because he was outstanding in his field.",
              3:"They don't have the guts.", 4:"An impasta.", 5:"Because it had too many problems.",
              6:"Nacho cheese.", 7:"Because then it would be a foot.", 8:"A gummy bear.",
              9:"Because it was two-tired.", 10:"I'll meet you at the corner."}

# Randomly generate jokes

key = random.randrange(10)

print("Joke: {}".format(jokes[key]))
print("Answer: {}".format(punchlines[key]))
