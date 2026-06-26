class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        Max_count = 0 

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                
            elif nums[i] == 0:
                if Max_count < count:
                    Max_count = count
                count = 0
        if count > Max_count:
                Max_count = count
            
        return Max_count


        