class Solution {
    public int minCost(String colors, int[] neededTime) {
        int i = 0, result=0, total, max;
        int n = colors.length();
        while(i<n){
            total = neededTime[i];
            max = neededTime[i];
            while(i+1<n && colors.charAt(i)==colors.charAt(i+1)){
                total+=neededTime[++i];
                max = Math.max(max,neededTime[i]);
            }
            result+=(total-max);
            i++;
        }
        return result;        
    }
}
