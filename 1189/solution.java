class Solution {
    public int maxNumberOfBalloons(String text) {
        Map<Character, Integer> map = new HashMap<>();
        map.put('b',0);
        map.put('a',0);
        map.put('l',0);
        map.put('o',0);
        map.put('n',0);
        char c;
        for(int i=0;i<text.length();i++){
            c = text.charAt(i);
            if(map.containsKey(c))
                map.put(c, map.get(c)+1);
        }
        int res = map.get('a');
        map.put('l', map.get('l')/2);
        map.put('o', map.get('o')/2);
        for(char ch: map.keySet())
            res = Math.min(res, map.get(ch));
        
        return res;
    }
}
