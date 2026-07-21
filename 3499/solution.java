class Solution {
    public int maxActiveSectionsAfterTrade(String s) {
        int ones = 0;
        int prev = Integer.MIN_VALUE;
        int curr = 0;
        int res = 0;
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='0')
                curr++;
            else{
                if(curr>0){
                    res = Math.max(res, curr+prev);
                    prev = curr;
                    curr = 0;
                }
                ones++;
            }
        }
        if(curr>0)
            res = Math.max(res, curr+prev);
        res+=ones;        
        return res;
    }
}
