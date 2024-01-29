words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 

def count_word_frequency(words):
    
    new_dict = {}
    
    for i in range(len(words)):
        if words[i] in new_dict:
            new_dict[words[i]] += 1
        else:
            new_dict[words[i]] = 1
            
    return new_dict


print(count_word_frequency(words))
    
    
    
#  {'apple': 3, 'orange': 2, 'banana': 1}