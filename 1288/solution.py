class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[0],-x[1]))
        res = len(intervals)
        lastInterval = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][1]<=lastInterval:
                res-=1
            else:
                lastInterval = intervals[i][1]
        return res
