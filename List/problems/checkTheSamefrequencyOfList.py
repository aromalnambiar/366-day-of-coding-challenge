list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]

def check_same_frequency(list1, list2):
    list1.sort()
    list2.sort()
    if len(list1) == len(list2):
        if list1 == list2:
            return True
        else:
            return False
    else:
        return False         

    
print(check_same_frequency(list1, list2))


# another method

def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter
        
    return count_elements(list1) == count_elements(list2)