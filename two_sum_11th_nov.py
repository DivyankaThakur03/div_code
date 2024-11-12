class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

                #time complexity: O(nsquare), space complexity: O(1)


#using hashmap to reduce time_complexity
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in num_map:
                return [num_map[complement], i]
            else:
                num_map[nums[i]] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            sum_num = nums[left] + nums[right]
            if sum_num == target:
                return [left +1 , right +1]
            elif sum_num < target:
                left +=1
            else:
                right -=1


