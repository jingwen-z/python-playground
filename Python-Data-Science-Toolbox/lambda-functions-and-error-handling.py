"""
Lambda functions and error-handling
"""

from functools import reduce

"""
Lambda functions
"""
# Define echo_word as a lambda function: echo_word
echo_word = lambda word1, echo: word1 * echo

# Call echo_word: result
result = echo_word('hey', 5)

# Print result
print(result)

# Map() and lambda functions
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells: shout_spells
shout_spells = map(lambda item: item + '!!!', spells)

# Convert shout_spells to a list: shout_spells_list
shout_spells_list = list(shout_spells)

# Convert shout_spells into a list and print it
print(shout_spells_list)

# Filter() and lambda functions
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Use filter() to apply a lambda function over fellowship: result
result = filter(lambda member: len(member) > 6, fellowship)

# Convert result to a list: result_list
result_list = list(result)

# Convert result into a list and print it
print(result_list)

# Reduce() and lambda functions
stark = ['robb', 'sansa', 'arya', 'eddard', 'jon']

# Use reduce() to apply a lambda function over stark: result
result = reduce(lambda item1, item2: item1 + item2, stark)

# Print the result
print(result)
