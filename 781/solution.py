from collections import defaultdict
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        vis = set()
        di = defaultdict(int)
        for i in answers:
            if i==0:
                res+=1
            elif not i in di:
                res+=(i+1)
                di[i] = 1
            else:
                di[i]+=1
                if i==di[i]-1:
                    del di[i]
        return res
        
