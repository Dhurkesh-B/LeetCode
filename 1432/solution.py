class Solution:
    def maxDiff(self, num: int) -> int:
        maxi = str(num)
        i = 0
        while i<len(maxi) and maxi[i]=='9':
            i+=1
        if i<len(maxi):
            maxi = maxi.replace(maxi[i],'9')
        maxi = maxi.replace(maxi[0],'9')
        mini =str(num)
        if mini[0]!='1':
            mini = mini.replace(mini[0],'1')
        else:
            i = 1
            while i<len(mini) and (mini[i]=='0' or mini[i]=='1'):
                i+=1
            if i<len(mini) :
                mini = mini.replace(mini[i],'0')
        return int(maxi)-int(mini)
