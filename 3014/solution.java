class Solution {
    public int minimumPushes(String word) {
        int res = 0;
        for(int i=0;i<word.length();i++)
            res+=1+i/8;
        return res;        
    }
}
