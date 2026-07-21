class Solution {
    public int maxActiveSectionsAfterTrade(String s) {
        int ones = 0;
        int curr = 0;
        int res = 0;
        List<Integer> zeros = new ArrayList<>();
        
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='0')
                curr++;
            else{
                if(curr>0){
                    zeros.add(curr);
                    curr = 0;   
                }
                ones++;
            }
        }
        if(curr>0)
            zeros.add(curr);
        
        for(int i=1;i<zeros.size();i++)
            res = Math.max(res, zeros.get(i-1)+zeros.get(i));
        return res+ones;
    }
}
