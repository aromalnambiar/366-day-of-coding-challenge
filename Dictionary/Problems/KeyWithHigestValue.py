my_dict = {'a': 5, 'b': 9, 'c': 2}


def max_value_key(my_dict):
    total = 0
    max_key = ''
    
    for keys, values in my_dict.items():
        if values > total:
            total = values
            max_key = keys
            
    return max_key

print(max_value_key(my_dict))


# another method

def max_value_key(my_dict):
    return max(my_dict, key=my_dict.get)

print(max_value_key(my_dict))