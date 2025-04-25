from collections import defaultdict
from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], mod: int, k: int) -> int:
        prefix = 0
        count_map = defaultdict(int)
        count_map[0] = 1  # handle case when prefix itself is valid
        result = 0

        for num in nums:
            if num % mod == k:
                prefix += 1
            
            # prefix % mod gives us cnt % mod so far
            # we want (prefix - k) % mod in earlier prefixes
            key = (prefix - k) % mod
            result += count_map[key]

            # store current prefix % mod in map
            count_map[prefix % mod] += 1

        return result
