class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        clusterNo = 1
        clusters = [1]
        res = []
        for i in range(1,n):
            if nums[i]-nums[i-1]>maxDiff:
                clusterNo+=1
            clusters.append(clusterNo)
        for u,v in queries:
            if clusters[u]==clusters[v] or u==v:
                res.append(True)
            else:
                res.append(False)
        return res
        

