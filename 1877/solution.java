class Solution {
  public int minPairSum(int[] nums) {
    Arrays.sort(nums);
    int result = 0;
    int n = nums.length;
    for (int i = 0; i < n / 2; i++)
      result = Math.max(result, nums[i] + nums[n - 1 - i]);
    return result;
  }
}
