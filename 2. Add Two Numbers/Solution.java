public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int rem = 0;
        ListNode head = l1;
        ListNode dummy = head;

        while((l1 != null) && (l2 != null)) {
            l1.val = l1.val + l2.val + rem;
            rem = l1.val / 10;
            l1.val = l1.val % 10;

            if(l1.next == null && l2.next != null) {
                l1.next = new ListNode(0);
            }
            l1 = l1.next;

            if(l2.next == null && l1 != null) {
                l2.next = new ListNode(0);
            }
            l2 = l2.next;
        }
        
        if(rem != 0) {
            while(dummy.next != null) {
                dummy = dummy.next;
            }
    
            dummy.next = new ListNode(rem);
        }

        return head;
    }
}
