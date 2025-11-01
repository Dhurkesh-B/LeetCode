class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        while head and head.val in nums:
            head = head.next
        root = head
        while head:
            if head.next and head.next.val in nums:
                head.next = head.next.next
            else:
                head = head.next
        return root
