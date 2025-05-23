class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        deltas = [(num ^ k) - num for num in nums]
        base_sum = sum(nums)
        
        # Sort deltas in decreasing order
        deltas.sort(reverse=True)
        
        max_gain = 0
        i = 0
        while i + 1 < len(deltas) and deltas[i] + deltas[i+1] > 0:
            max_gain += deltas[i] + deltas[i+1]
            i += 2

        return base_sum + max_gain
