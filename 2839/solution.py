class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        odd1 = '' 
        odd2 = '' 
        even1 = '' 
        even2 = ''
        for i in range(4):
            if i%2:
                odd1+=s1[i]
                odd2+=s2[i]
            else:
                even1+=s1[i]
                even2+=s2[i]
        return sorted(odd1)==sorted(odd2) and sorted(even1)==sorted(even2)
