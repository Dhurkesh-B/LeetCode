class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = [startTime[0]]
        for i in range(1, len(startTime)):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])

        prefs = [gaps[0]]
        for i in range(1, len(gaps) - 1):
            prefs.append(max(prefs[-1], gaps[i]))
        
        suffs = [gaps[-1]]
        for i in range(len(gaps) - 2, 0, -1):
            suffs.append(max(suffs[-1], gaps[i]))
        suffs = list(reversed(suffs))

        ans, N = 0, len(startTime)

        for i, (start, end) in enumerate(zip(startTime, endTime)):
            slot = end - start
            lGap, rGap = gaps[i], gaps[i + 1]
            bestLeft = -1 if i == 0 else prefs[i - 1]
            bestRight = -1 if i == N - 1 else suffs[i + 1]
            time = lGap + rGap
            if bestLeft >= slot or bestRight >= slot:
                time += slot
            ans = max(ans, time)
        
        return ans
