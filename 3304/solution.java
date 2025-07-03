class Solution {
    public char kthCharacter(int k) {
        String word = "a";
        char c = 'a';
        String curr = "";
        Map<Character,Character> nextChar = new HashMap<>();
        for(int i=97;i<123;i++)
            nextChar.put((char)i,(char)(i+1));
        nextChar.put('z','a');
        while(word.length()<k){
            curr = "";
            for(int i=0;i<word.length();i++){
                c = word.charAt(i);
                curr =curr+c+nextChar.get(c);
            }
            word = curr;
        }
        return word.charAt(k-1);        
    }
}
