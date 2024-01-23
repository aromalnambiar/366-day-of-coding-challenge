import numpy as np

# Creating 2D array
twoDimensionalArray = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8], [9, 10, 11]])


# delete elementing from array using numpy delete method
deletingElement = np.delete(twoDimensionalArray, 0, axis=1)

print(deletingElement)

