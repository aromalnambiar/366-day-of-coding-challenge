myList = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target = 7

def pair_sum(nums, target):
    data = []
    
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] + nums[j] == target:
                data.append(f"{nums[i]}  +  {nums[j]}")
    
    return data        
        
print(pair_sum(myList, target))     
