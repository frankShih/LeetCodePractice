/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        /*
        // 100%
        if (head == null || head.next==null) {
            return false;
        }
        ListNode slow = head, fast = head;
        while(fast.next != null && fast.next.next != null){
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast) {
                return true;
            }
        }
        return false;
        */

        // 4%
        Set<ListNode> nodes = new HashSet<>();
        while(head!=null) {
            if (nodes.contains(head)) {
                return true;
            } else {
                nodes.add(head);    
                head=head.next;
            }
            
        }
        return false;
    }
}