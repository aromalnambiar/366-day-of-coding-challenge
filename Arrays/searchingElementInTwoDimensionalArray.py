import numpy as np

# Creating an array
newArray = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]) 


# funtion for searching an element in the array
def findArray(array, element):
    # TC - O(mn) , SC - O(1)
    for i in range(len(array)): 
        # TC - O(n) , SC - O(1)
        for j in range(len(array[0])):
            # TC - O(1) , SC - O(1)
            if array[i][j] == element:
                return "The position of the element " + str(element) + " is " + str(i) + " " + str(j)
    return "Element not found in the array"


print(findArray(newArray, 10))

# So TC - O(n^2) and SC - O(1)
