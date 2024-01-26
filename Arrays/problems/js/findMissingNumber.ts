
var twoSum = function(nums: number[], target: number) {
    let data = {};

    for(let i = 0; i < nums.length ; i++){
        let num = nums[i]
        let complement = target - num

        if(complement in data){
            return([data[complement], i])
        }

        data[num] = i
    }

};

let nums = [2,7,11,15]
let target = 9
let result = twoSum(nums, target)

console.log(result)