class Solution {
    public long sumAndMultiply(int n) {
        int x = 0;
        int sum = 0;
        int i = 1;
        int d;
        while(n>0){
            d = n%10;
            n/=10;
            if(d==0)
                continue;
            x = d*i + x;
            sum+=d;
            i*=10;
        }
        return (long)sum*x;
    }
}
