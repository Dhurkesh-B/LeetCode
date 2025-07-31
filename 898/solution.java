class Solution {
    public int subarrayBitwiseORs(int[] arr) {
        Set<Integer> result = new HashSet<>();
        Set<Integer> prev = new HashSet<>();
        for(int i: arr){
            Set<Integer> next = new HashSet<>();
            next.add(i);
            for(int p:prev)
                next.add(p|i);
            prev = next;
            result.addAll(prev);
        }
        return result.size();
    }
}
