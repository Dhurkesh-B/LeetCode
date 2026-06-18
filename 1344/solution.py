class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        res = abs(30*hour - 5.5*minutes)
        return min(res, 360-res)
