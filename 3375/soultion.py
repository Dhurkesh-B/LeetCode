import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums)<k:
            return -1
        nums = set(nums)
        heap = []
        for i in nums:
            heapq.heappush(heap,-i)
        res = 0
        while heap and heap[0]+k<0:
            val = (heapq.heappop(heap)*-1)-1
            heapq.heapify(heap)
            if heap:
                while val>(heap[0]*-1):
                    val-=1
                for i in range(len(heap)):
                    if heap[i]>val:
                        heap[i] = val
            res+=1
        return res
