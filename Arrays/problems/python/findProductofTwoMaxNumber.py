
my_list = [1, 2, 3, 10, 5, 6, 7, 8, 9]

def sumOfProduct(arr):
    arr.sort(reverse=True)
    return arr[0] * arr[1]


print(sumOfProduct(my_list))



# another method
 

def max_product(arr):
    max1, max2 = 0, 0
    
    for i in range(len(arr)):
        if max1 < arr[i]:
            max2 = max1
            max1 = arr[i]
        elif max2 < arr[i] and max1 != max2:
            max2 = arr[i]


    return max1 * max2


print(max_product(my_list))