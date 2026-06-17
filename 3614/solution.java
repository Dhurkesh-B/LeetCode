class Solution {
    public char processStr(String s, long k) {
        long length = 0;
        for(int i=0;i<s.length();i++){
            if(Character.isLetter(s.charAt(i)))
                length++;
            else if(s.charAt(i)=='#')
                length*=2;
            else if(s.charAt(i)=='*' && length>=1)
                length--;                
        }

        if(k>=length)
            return '.';
        for(int i=s.length()-1;i>=0;i--){
            if(Character.isLetter(s.charAt(i))){
                if(k+1==length)
                    return s.charAt(i);
                length--;
            }
            else if(s.charAt(i)=='#'){
                length/=2;
                k = k%length;
            }
            else if(s.charAt(i)=='*'){
                length++;
            }
            else if(s.charAt(i)=='%')
                k = length-k-1;
        }
        return '.';
    }
}
