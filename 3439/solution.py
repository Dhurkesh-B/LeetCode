from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        res = 0
        n = len(startTime)
        pre = [endTime[0]-startTime[0]]
        for i in range(1,n):
            pre.append(pre[-1]+endTime[i]-startTime[i])
        for i in range(k-1,n):
            left = endTime[i-k] if i-k>=0 else 0 
            right = startTime[i+1] if i+1<n else eventTime
            tot = pre[i] - (pre[i-k] if i-k>=0 else 0)
            res = max(res,right-left -tot)
        return res 

