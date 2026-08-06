class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def isProductDivisible(digit, t):
            curr = 1 
            while digit:
                curr = curr*(digit%10)
                digit//=10 
            return curr%t 
        
        res = n 
        while isProductDivisible(res, t):
            res+=1 
        return res
