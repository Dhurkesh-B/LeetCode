from collections import defaultdict
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        res = [0]
        cache = defaultdict(int)
        def func(i): 
            if i>=len(questions):
                return 0           
            else:
                if i in cache:
                    return cache[i]
                p1,p2 = questions[i]
                take = p1 + func(i+1+p2)
                skip = func(i+1)
                cache[i] = max(take,skip)
                return cache[i]
        return func(0)
                

        
