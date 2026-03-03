class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def reverseInvert(s):
            temp = ''
            for i in s:
                if i=='1':
                    temp+='0'
                else:
                    temp+='1'
            return temp[::-1]
        
        result = '0'
        for i in range(1,n):
            result = result + '1' +reverseInvert(result)
        return result[k-1]
