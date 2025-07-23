class Solution {
    private String s;
    public int removePair(String pair, int score){
        ArrayList<Character> stack = new ArrayList<>();
        stack.add('z'); 
        int result = 0;

        for(int i = 0; i < this.s.length(); i++){
            if(this.s.charAt(i) == pair.charAt(1) && stack.get(stack.size() - 1) == pair.charAt(0)){
                result += score;
                stack.remove(stack.size() - 1);
            } else {
                stack.add(this.s.charAt(i));
            }
        }

        StringBuilder sb = new StringBuilder();
        for(int i = 1; i < stack.size(); i++){
            sb.append(stack.get(i));
        }

        this.s = sb.toString();
        return result;
    }
    public int maximumGain(String s, int x, int y) {
        this.s = s;
        int result = 0;

        String temp = x > y ? "ab" : "ba";
        result += removePair(temp, Math.max(x, y));
        result += removePair(new StringBuilder(temp).reverse().toString(), Math.min(x, y));

        return result;
    
    }
}
