### Lists, what are they?

## Create a list
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]

# Print areas
print(areas)

## Create list with different types
# Adapt list areas
areas = ["hallway", hall, "kitchen", kit, "living room", liv,
         "bedroom", bed, "bathroom", bath]

# Print areas
print(areas)

## List of lists
# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))

### Subsetting lists

## Subset and conquer
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0,
         "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[1])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])
