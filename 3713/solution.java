class Solution {
    public int longestBalanced(String s) {
        Map<Character,Integer> map;
        int result = 0, n = s.length();
        int balance;
        for(int i=0;i<n;i++){
            map = new HashMap<>();
            balance = 0;
            for(int j=i;j<n;j++){
                map.put(s.charAt(j), map.getOrDefault(s.charAt(j),0)+1);
                int value = map.get(s.charAt(i));
                boolean same = true;
                for(char k:map.keySet()){
                    if(value!=map.get(k)){
                        same = false;
                        break;
                    }
                }
                if(same)
                    result = Math.max(result, j-i+1);
            }
        }
        return result;
    }
}
