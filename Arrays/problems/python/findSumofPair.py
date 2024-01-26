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