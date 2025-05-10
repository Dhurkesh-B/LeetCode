class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1 = nums1.count(0)
        z2 = nums2.count(0)
        s1 = sum(nums1)+z1
        s2 = sum(nums2)+z2
        if (z2==0 and s1>s2) or (z1==0 and s2>s1):
            return -1
        return max(s1,s2)
