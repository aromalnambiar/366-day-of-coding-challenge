my_dict = {'a': 1, 'b': 2, 'c': 3}

def reverse_dict(my_dict):
    return {v:k for k, v in my_dict.items()}

print(reverse_dict(my_dict))