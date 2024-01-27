import numpy as np

new_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
number = 5


def findNumber(arr, num):
    if num in arr:
        for i in range(len(arr)): 
            if arr[i] == num:
                    print(i)
    else:
        print("Number doesn't exist in array")
            
            
findNumber(new_array, number)