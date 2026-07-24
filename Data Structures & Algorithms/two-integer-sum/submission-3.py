class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        for i in range (len(nums)):
            sum_part = target - nums[i]
            if sum_part in dict_nums:
                return [dict_nums[sum_part], i]
            else:
                dict_nums[nums[i]] = i

         
        