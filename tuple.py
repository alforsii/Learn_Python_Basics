# Tuples cannot be modified
coordinates = (4, 5, 7, 9)
# coordinates[1] = 55 # TypeError: 'tuple' object does not support item assignment
print(coordinates[0], coordinates[1], coordinates[2], coordinates[3])

# but we can make modify a list/array of tuples
coordinates2 = [(4, 5), (6, 7), (80, 9)]
coordinates2[0] = (5, 7)
print(coordinates2)


