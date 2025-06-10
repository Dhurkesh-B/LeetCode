from collections import defaultdict
class Solution:
    def maxDifference(self, s: str) -> int:
        counter = defaultdict(int)
        for i in s:
            counter[i]+=1
        oddCount = -1
        evenCount = float('inf')
        for i in counter.values():      
            if i%2:
                oddCount = max(oddCount,i)
            else:
                evenCount = min(evenCount,i)
        if evenCount==float('inf'):
            evenCount = 0
        return oddCount-evenCount
        

