from typing import List
from sortedcontainers import SortedList

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        sl = SortedList()
        d = {v: i for i, v in enumerate(nums1)}  # Map nums1 values to indices
        res = 0
        
        for i in range(1, n - 1):
            sl.add(d[nums2[i - 1]])
            z = d[nums2[i]]
            x = sl.bisect_left(z)  # Count of elements smaller than z
            y = (n - 1 - z) - (len(sl) - x)  # Count of elements greater than z that are still unprocessed
            res += x * y
        
        return res
