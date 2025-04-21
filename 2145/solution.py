class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        mx,mi = 0,0
        val = 0
        n = len(differences)
        for diff in  differences:
            val+=diff
            mx = max(val,mx)
            mi = min(val,mi)
        diff = mx - mi
        return max(0,(upper-lower)-diff+1)

