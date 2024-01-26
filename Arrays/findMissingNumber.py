import numpy as np

new_array = [1, 2, 3, 4, 6]
no_elements = 6

def missing_number(arr, n):
    # equation for find the total sum of n numbers
    total = n * (n + 1) // 2
    # sum function for find the total sum of the list
    sum_array = sum(arr)
    
    find_number = total - sum_array
    
    return find_number

print(missing_number(new_array, no_elements))