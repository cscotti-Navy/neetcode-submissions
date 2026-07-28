import heapq 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        heap = []
    
        for num in nums:
            if num in count:
                count[num] += 1
        
            else:
                count[num] = 1

        for num, freq in count.items():
            if len(heap) < k:
                heapq.heappush(heap,(freq,num))

            else:
                if (freq,num) > heap[0]:
                    heapq.heapreplace(heap, (freq,num))
        result = [i[1] for i in heap]
        return result 
