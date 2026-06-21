class Solution {
    public int maxIceCream(int[] costs, int coins) {
        int res = 0;
        Arrays.sort(costs);
        int ind = 0;
        while(ind<costs.length && coins>=costs[ind]){
            res++;
            coins-=costs[ind++];
        }
        return res;
    }
}
