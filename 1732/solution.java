class Solution {
    public int largestAltitude(int[] gain) {
        int altitude = 0;
        int res = 0;
        for(int i: gain){
            altitude+=i;
            res = Math.max(res, altitude);
        }
        return res;
    }
}
