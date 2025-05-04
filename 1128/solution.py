from collections import defaultdict
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        di = defaultdict(int)
        res = 0
        for i in range(len(dominoes)):
            val = tuple(sorted(dominoes[i]))
            dominoes[i] = val
        for i in dominoes:
            di[i]+=1
            res+=(di[i]-1)
        return res
