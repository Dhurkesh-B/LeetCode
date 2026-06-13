class Solution {
    public String mapWordWeights(String[] words, int[] weights) {
        Map<Character, Integer> cmap = new HashMap<>();
        Map<Integer, Character> vmap = new HashMap<>();
        char c;
        int curr;
        String res = "";
        for(int i=0;i<26;i++){
            c =(char) (97+i);
            cmap.put(c, weights[i]);
            vmap.put(25-i,c);
        }
        System.out.println(vmap);

        for(String word: words){
            curr = 0;
            for(int i=0;i<word.length();i++)
                curr+=cmap.get(word.charAt(i));
            res+=vmap.get(curr%26);
        }
        return res;  
    }
}
