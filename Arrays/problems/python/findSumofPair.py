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
class Solution:
    def twoSum(self, arr, t):
         # empty dictionary
        data = {}

        # i represents the index and num represents the elements in array of nums. The enumarate funtion will iterate throught the all element in the list
        for i , num in enumerate(arr):
            # find the complement
            complement = t - num

            if complement in data:
                return [data[complement], i]

            data[num] = i

nums = [2,7,11,15]
target = 9
sol = Solution()
result = sol.twoSum(my_list, target)
print(result)

        