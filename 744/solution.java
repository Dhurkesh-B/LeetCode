class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        char result = '{';
        for(char c:letters){
            if(c>itarget && c<result)
                result = c;
        }
        if(result=='{')
            return letters[0];
        return result;
    }
}
