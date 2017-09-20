"""
Default arguments, variable-length arguments and scope
"""

"""
Scope and user-defined functions
"""
# The keyword global
# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    # Use team in global scope
    global team

    # Change the value of team in global: team
    team = "justice league"

# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)

"""
Nested functions
"""
# Nested Functions I
# Define three_shouts
def three_shouts(word1, word2, word3):

    # Define inner
    def inner(word):
        return word + '!!!'

    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))

# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))

# Nested Functions II
# Define echo
def echo(n):
    """Return the inner_echo function."""

    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word

    # Return inner_echo
    return inner_echo


# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))

# The keyword nonlocal and nested functions
# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""

    # Concatenate word with itself: echo_word
    echo_word = word + word

    #Print echo_word
    print(echo_word)

    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""
        #Use echo_word in nonlocal scope
        nonlocal echo_word

        #Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'

    # Call function shout()
    shout()

    #Print echo_word
    print(echo_word)

#Call function echo_shout() with argument 'hello'
echo_shout('hello')
