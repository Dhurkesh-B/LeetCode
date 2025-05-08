import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # visited[x][y][parity] = whether we've visited cell (x, y) with this parity (0 for 1s move, 1 for 2s move)
        visited = [[[False, False] for _ in range(m)] for _ in range(n)]
        
        # heap elements are (time, x, y, parity) where parity 0 means next move is 1s, 1 means 2s
        heap = [(0, 0, 0, 0)]  # start at (0,0) with time 0 and 1-second move next
        
        while heap:
            time, x, y, parity = heapq.heappop(heap)
            
            if x == n - 1 and y == m - 1:
                return time
            
            if visited[x][y][parity]:
                continue
            visited[x][y][parity] = True
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < m:
                    wait_time = max(time, moveTime[nx][ny])
                    move_duration = 1 if parity == 0 else 2
                    next_time = wait_time + move_duration
                    next_parity = 1 - parity
                    
                    if not visited[nx][ny][next_parity]:
                        heapq.heappush(heap, (next_time, nx, ny, next_parity))
        
        return -1  # in case there's no path (though constraints guarantee a path exists)
