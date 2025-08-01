class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> nums = new ArrayList();
        nums.add(new ArrayList<>(Arrays.asList(1)));
        if(numRows==1)
            return nums;
        nums.add(new ArrayList<>(Arrays.asList(1,1)));
        int n;
        while(nums.size()<numRows){
            nums.add(new ArrayList<>(Arrays.asList(1)));
            n = nums.size();
            for(int i=0;i<nums.get(n-2).size()-1;i++)
                nums.get(n-1).add(nums.get(n-2).get(i)+nums.get(n-2).get(i+1));
            nums.get(n-1).add(1);
        }
        return nums;
    }
}
