from collections import defaultdict
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        def bfs():
            res = 0
            q = initialBoxes
            waitingbox = set(initialBoxes)
            currKey = set()
            vis = set()
            openCount = set()
            vis = set()
            for i in range(len(status)):
                if status[i]:
                    openCount.add(i)
            while True:
                opened = False
                n = len(q)
                for _ in range(n):
                    box = q.pop(0)
                    if box in vis:
                        continue
                    if box in openCount or box in currKey:
                        res+=candies[box]
                        vis.add(box)
                        opened = True
                        for k in keys[box]:
                            if k not in currKey:
                                currKey.add(k)
                                if k in waitingbox and k not in vis:
                                    q.append(k)
                        for b in containedBoxes[box]:
                            if not b in waitingbox:
                                waitingbox.add(b)
                                q.append(b)
                    else:
                        q.append(box)
                if not opened:
                    break
            return res

          
        return bfs()
