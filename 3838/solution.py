class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        di = {}
        ci = {}
        for i in range(26):
            di[chr(97+i)] = weights[i]
            ci[25-i] = chr(97+i)
        res = ''
        for word in words:
            curr = 0
            for c in word:
                curr+=di[c]
            res+=ci[curr%26]
        return res
