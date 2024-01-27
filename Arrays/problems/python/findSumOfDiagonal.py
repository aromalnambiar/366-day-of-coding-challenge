
my_list = [[1,2,3],[4,5,6],[7,8,9]] 

def diagonal_sum(matrix):
    place = 0
    sum = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == place:
                sum = sum + matrix[i][place]
        place = place + 1

    return sum


print(diagonal_sum(my_list))



# another method

def diagonal_sum_another(matrix):
        
    total = 0
    for i in range(len(matrix)):
         total += matrix[i][i]
     
    return total

print(diagonal_sum_another(my_list))