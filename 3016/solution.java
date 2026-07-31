class Solution {
    public int minimumPushes(String word) {
        Map<Character, Integer> map = new HashMap<>();
        int res = 0;
        int cnt = 0;
        for(int i=0;i<word.length();i++){
            char c = word.charAt(i);
            map.put(c, map.getOrDefault(c,0)+1);
        }
        List<Map.Entry<Character, Integer>> keys = new ArrayList<>(map.entrySet());
        keys.sort(Map.Entry.<Character, Integer>comparingByValue().reversed());
        for(Map.Entry<Character, Integer> entry: keys)
            res+=entry.getValue()*(1+cnt++/8);
        return res;
    }
}
