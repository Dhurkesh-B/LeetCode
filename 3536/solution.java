class Solution {
    public int maxProduct(int n) {
        int res = 0;
        int m = 0;
        int d;
        while(n>0){
            d = n%10;
            res = Math.max(res, d*m);
            m = Math.max(m, d);
            n/=10;
        }
        return res;
    }
}
