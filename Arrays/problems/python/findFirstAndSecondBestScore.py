myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]


def first_second(my_list):
    max1 ,max2 = 0, 0
    
    
    for i in range(len(my_list)):
        if my_list[i] > max1:
            max2 = max1
            max1 = my_list[i]
            
        elif my_list[i] > max2 and max2 != max1:
            max2 = my_list[i]
            
            
    return max1, max2
    
    
print(first_second(myList))