"""
Merge Names (Easy)
"""


# Implement the unique_names method. When passed two lists of names, it will
# return a list containing the names that appear in either or both lists. The
# returned list should have no duplicates.
#
# For example, calling unique_names(['Ava', 'Emma', 'Olivia'],
# ['Olivia', 'Sophia', 'Emma']) should return a list containing Ava, Emma,
# Olivia, and Sophia in any order.

def unique_names(names1, names2):
    result = list()
    for m in names1:
        if (m in result) == False:
            result.append(m)
    for n in names2:
        if (n in result) == False:
            result.append(n)
    return result


names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2))  # should print Ava, Emma, Olivia, Sophia
