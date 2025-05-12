from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        for per in permutations(digits,3):
            if per[0]==0 or per[-1]%2:
                continue
            val = per[0]*100+per[1]*10 + per[2]
            res.add(val)
        return sorted(list(res))
