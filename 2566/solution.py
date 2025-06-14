class Solution:
    def minMaxDifference(self, num: int) -> int:
        maxi = str(num)
        mini = str(num)
        i = 0
        while i<len(maxi) and maxi[i]=='9':
            i+=1
        if i<len(maxi):
            maxi = maxi.replace(maxi[i],'9')
        mini = mini.replace(mini[0],'0')
        return int(maxi)-int(mini)
