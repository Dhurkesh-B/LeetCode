import heapq
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        heap = []
        heapq.heappush(heap,nums[0])
        res = -1
        for i in range(1,len(nums)):
            val = heap[0]
            res = max(nums[i]-val,res)
            heapq.heappush(heap,nums[i])
        if res==0:
            return -1
        return res
