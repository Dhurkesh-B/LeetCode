class Solution:
    def numSteps(self, s: str) -> int:
        result = 0
        val = int(s,2)
        while val>1:
            if val%2:
                val+=1
            else:
                val//=2
            result+=1
        return result
