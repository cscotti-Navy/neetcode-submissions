class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1 

        for i in range(len(arr) -1, -1, -1):
            original_value = arr[i]
            arr[i] = rightMax

            if original_value > rightMax:
                 rightMax = original_value
        return arr
            
                


