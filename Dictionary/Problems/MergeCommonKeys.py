dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

def merge_dicts(d1, d2):
    
    new_dict = {}
    
    for i, keys1 in enumerate(d1):
        for j, keys2 in enumerate(d2):
            
            if keys1 == keys2:
                d1[keys1] += d2[keys2]
            else:
                new_dict[keys1] = d1[keys1] 
                
            if keys2 not in d1 and i == (len(d1) - 1):
                new_dict[keys2] = d2[keys2]    
    return new_dict


print(merge_dicts(dict1, dict2))        



# another method
def merge_dicts_another(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result


print(merge_dicts_another(dict1, dict2))