class Solution {
    public String smallestPalindrome(String s) {
        int n = s.length();
        int[] freq = new int[26];
        char[] res = new char[n];

        for(char c: s.toCharArray())
            freq[c-'a']++;

        int left = 0;
        int right = n-1;

        for(int i=0;i<26;i++){
            char c = (char) (i+'a');
            while(freq[i]>=2){
                res[left++] = c;
                res[right--] = c;
                freq[i]-=2;
            }
        }

        for(int i=0;i<26;i++){
            if(freq[i]==1){
                res[left] = (char) (i+'a');
                break;
            }
        }
        return new String(res);
    }
}
