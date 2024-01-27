
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def sumOfProduct(arr):
    arr.sort(reverse=True)
    return arr[0] * arr[1]


print(sumOfProduct(my_list))