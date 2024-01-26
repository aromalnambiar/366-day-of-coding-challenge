my_list = [1, 2, 4, 2, 7, 2, 9]
target = 5


def find_sum_pair(nums, target):
    
    for i in range(len(nums)):
        for j in range(i + 1  ,len(nums)):
            if nums[i] == nums[j]:
                continue
            elif nums[i] + nums[j] == target:
                print([nums[i], nums[j]])
                
find_sum_pair(my_list, target)



# another method using dictionary and enumarate funtion

def find_pair_ans(nums, target):
    # empty dictionary
    data = {}
    
    # i represents the index and num represents the elements in array of nums. The enumarate funtion will iterate throught the all element in the list
    for i, num in enumerate(nums):
        # find the complement
        complement = target - num
        
        if complement in data:
            print(f"Indices of the two numbers are: {[data[complement], i]}")
        
        data[num] = i
        
        
find_pair_ans(my_list, target)