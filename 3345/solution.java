class Solution {

    boolean isProductDivisible(int digit, int t){
        int curr = 1;
        while(digit>0){
            curr = curr * (digit%10);
            digit/=10;
        }
        return curr%t==0;
    }
    
    public int smallestNumber(int n, int t) {
        int res = n;
        while(!isProductDivisible(res,t))
            res++;
        return res;
    }
}
