import heapq
from typing import List

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        active = []  # Min-heap to track currently active queries by end index
        candidates = []  # Max-heap to store future usable queries (by end index, negated)
        
        # Sort queries based on their starting index
        queries.sort(key=lambda q: q[0])
        
        q_idx = 0  # Index for iterating through sorted queries
        total_used = 0  # Count of queries that were applied
        
        for idx in range(n):
            # Add all queries starting at current index to candidates heap
            while q_idx < len(queries) and queries[q_idx][0] == idx:
                heapq.heappush(candidates, -queries[q_idx][1])
                q_idx += 1
            
            # Decrease the current number by the count of active queries
            nums[idx] -= len(active)
            
            # Apply additional queries if needed to reduce nums[idx] to zero
            while nums[idx] > 0 and candidates and -candidates[0] >= idx:
                heapq.heappush(active, -heapq.heappop(candidates))
                nums[idx] -= 1
                total_used += 1
            
            # If not enough coverage to zero out nums[idx], return failure
            if nums[idx] > 0:
                return -1
            
            # Clean up any queries in active heap that end at the current index
            while active and active[0] == idx:
                heapq.heappop(active)
        
        # The answer is the count of queries that can be removed
        return len(queries) - total_used
