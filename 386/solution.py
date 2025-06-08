class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return list(sorted(range(1,n+1),key=lambda x:str(x)))
