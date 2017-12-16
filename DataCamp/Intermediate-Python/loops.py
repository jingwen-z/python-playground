"""
Loops
"""

import numpy as np
import pandas as pd

"""
while loop
"""
# Basic while loop
offset = 8

# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)

# Add conditionals
# Initialize offset
offset = -6

# Code the while loop
while offset != 0:
    print("correcting...")
    if offset > 0:
        offset = offset - 1
    else:
        offset = offset + 1
    print(offset)

"""
for loop
"""
# Loop over a list
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for area in areas:
    print(area)

# Indexes and values
# Change for loop to use enumerate()
for index, area in enumerate(areas):
    print("room " + str(index) + ": " + str(area))

# Loop over list of lists
# house list of lists
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

# Build a for loop from scratch
for room, area in house:
    print("the " + str(room) + " is " + str(area) + " sqm ")

"""
Looping Data Structures
"""
# Loop over dictionary
# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'bonn',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw', 'australia': 'vienna'}

# Iterate over europe
for key, value in europe.items():
    print("the capital of " + str(key) + " is " + str(value))

# Loop over Numpy array
# For loop over np_height
for height in np_height:
    print(str(height) + " inches")

# For loop over np_baseball
for mesures in np.nditer(np_baseball):
    print(mesures)

# Loop over DataFrame
cars = pd.read_csv('cars.csv', index_col=0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)

# Adapt for loop
for lab, row in cars.iterrows():
    print(lab + ": " + str(row["cars_per_cap"]))

# Add column
# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

# Print cars
print(cars)
