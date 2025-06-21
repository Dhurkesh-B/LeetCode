class Solution {
    public int minimumDeletions(String word, int k) {
        int[] charCounter = new int[26];
        int result = Integer.MAX_VALUE;
        for(int i=0;i<word.length();i++){
            charCounter[(int)word.charAt(i)-97]++;
        }
        ArrayList<Integer> nums = new ArrayList<>();
        ArrayList<Integer> ps = new ArrayList<>();
        for(int i:charCounter){
            if(i>0)
                nums.add(i);
        }
        Collections.sort(nums);
        ps.add(0);
        for(int i=1;i<=nums.size();i++)
            ps.add(ps.get(i-1)+nums.get(i-1));
        int n = nums.size();
        for(int i=0;i<n;i++){
            int deletions = ps.get(i);
            for(int j=i;j<n;j++){
                if(nums.get(j)-nums.get(i)>k)
                    deletions+=(nums.get(j)-nums.get(i)-k);
            }
            result = Math.min(deletions,result);
        }
        return result;
    }
}
