class Solution:
    def minPartitions(self, n: str) -> int:
        result = '0'
        for i in n:
            if i>result:
                result = i
        return int(result)
