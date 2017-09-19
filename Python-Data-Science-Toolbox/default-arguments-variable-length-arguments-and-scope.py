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
