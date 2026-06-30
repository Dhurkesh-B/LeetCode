class Solution {
    public int numberOfSubstrings(String s) {
        int[] arr = {0,0,0};
        int i, l=0, n=s.length(), res=0;
        for(int r=0;r<n;r++){
            i = (int) s.charAt(r)-97; 
            arr[i]++;
            while(arr[0]>=1 && arr[1]>=1 && arr[2]>=1){
                res+=(n-r);
                i = (int) s.charAt(l)-97;
                arr[i]--;
                l++; 
            }
        }
        return res;
    }
}
