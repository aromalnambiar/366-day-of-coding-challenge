myMatrix = [[1,2,3],
            [4,5,6],
            [7,8,9]]




def rotate(matrix):

    rotated_matrix = [[]]
    length = len(matrix) - 1
    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            rotated_matrix[i].append(matrix[length - j][i])
            
        if (i + 1) == len(matrix):
            continue
        else:
            rotated_matrix.append([])
            
    rotated_matrix = matrix  
           
    return matrix 
        
print(rotate(myMatrix))



# another method

def rotate_another(matrix):
    n = len(matrix)
 
    
    for i in range(n):  
        for j in range(i, n):  
            
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
 
    
    for row in matrix: 
        row.reverse() 
     
    return matrix   


print(rotate_another(myMatrix))