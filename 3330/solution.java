class Solution {
    public int possibleStringCount(String word) {
        int n = word.length(), res = 1, i = 0,j;
        while(i<n){
            j = i;
            while(j+1<n && word.charAt(i)==word.charAt(j+1))
                j++;
            if(j>i){
                res+=(j-i);
                i = j;
            }
            i++;
        }
        return res;        
    }
}
