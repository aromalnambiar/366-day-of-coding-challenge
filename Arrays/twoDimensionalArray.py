import numpy as np

# Create 2D array
twoDimensionalArray = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8], [9, 10, 11]])


# Inserting elements in 2D arrays
# np.insert("main array","index position where the array would be inserted", "array element", axis 1 is inserting element in the row and axis 2 is inserting element in the column element in colum)
newToArray = np.insert(twoDimensionalArray, 0, [[-2, -1, 0]], axis=0)
# newTo2Array = np.insert(twoDimensionalArray, 1, [[-5, -4, -3]], axis=1)

print(newToArray)
# print(newTo2Array)


# Appeding array using append method
# its only append the element only on the last
newAppendToArray = np.append(twoDimensionalArray, [[12, 13, 14]] , axis=0)
print(newAppendToArray)

