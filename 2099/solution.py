
from collections import defaultdict
import heapq
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        vis = defaultdict(int)
        collect = defaultdict(int)
        for i in nums:
            heapq.heappush(heap,-i)
        for _ in range(k):
            vis[-heapq.heappop(heap)]+=1
        for i in nums:
            if i in vis and collect[i]<vis[i]:
                res.append(i)
                collect[i]+=1
        return res
