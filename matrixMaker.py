"""
This file is used exclusively to make an *almost complete matrix including all regions.
"""

from regionDict import regionDict

# Creates a 432x432 matrix with -1 as the default value.
# matrix = [[-1 for _ in range(432)] for _ in range(432)]

dictLength = len(regionDict)

regionMatrix = [[['key', 'key2', []] for _ in range(dictLength)] for _ in range(dictLength)]

keys = []
for key in regionDict:
    keys.append(key)

# Assign the keys of the dictionary to the array
for i in range(dictLength):
    for j in range(dictLength):
        regionMatrix[i][j][0] = keys[i]
        regionMatrix[i][j][1] = keys[j]

        if i == j:
            regionMatrix[i][j][2].append("You asked how to get from region 'x' to region 'x', you are already in region 'x'.")


for row in regionMatrix:
    print(row, end="")
    print(",")

