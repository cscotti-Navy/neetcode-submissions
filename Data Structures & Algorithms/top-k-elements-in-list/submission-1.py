class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
        
            else:
                count[num] = 1

        my_list = sorted((count.items()), key = lambda pair: pair[1], reverse=True)

        top_pairs = my_list[:k]

        result = [i[0] for i in top_pairs]

        return result 

        