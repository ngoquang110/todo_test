from parse import pars
import random

# Ask the user to enter a lower and an upper bound divided by a comma
user_input = input("Enter a lower bound and an uppwer bound divided a comma (e.g., 2,10)")

# Parse the user string by calling the parse function
parsed = pars(user_input)

# Pick a random int between the two numbers
rand = random.randint(parsed['lower_bound'], parsed['gitupper_bound'])

print(rand)