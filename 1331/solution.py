class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = 1 
        nums = sorted(arr)
        rankMap = {}
        for i in nums:
            if i not in rankMap:
                rankMap[i] = rank
                rank+=1 
        for i in range(len(arr)):
            arr[i] = rankMap[arr[i]]
        return arr
