class Solution {
    public int pairSum(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        ListNode prev = null;
        ListNode temp = null;
        int res = 0;
        while(fast!=null && fast.next!=null){
            fast = fast.next.next;
            temp = slow.next;
            slow.next = prev;
            prev = slow;
            slow = temp; 
        }

        while(slow!=null){
            res = Math.max(res, slow.val+prev.val);
            prev = prev.next;
            slow = slow.next;
        }
        return res;
        
    }
}
