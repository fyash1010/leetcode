import static org.junit.Assert.assertEquals;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.junit.*;

public class Main {
    @Test
    public void testAddTwoNumbers() {
        // Construct l1 = [9, 9, 9, 9, 9, 9, 9]
        ListNode l1 = new ListNode(9);
        l1.next = new ListNode(9);
        l1.next.next = new ListNode(9);
        l1.next.next.next = new ListNode(9);
        l1.next.next.next.next = new ListNode(9);
        l1.next.next.next.next.next = new ListNode(9);
        l1.next.next.next.next.next.next = new ListNode(9);

        // Construct l2 = [9, 9, 9, 9]
        ListNode l2 = new ListNode(9);
        l2.next = new ListNode(9);
        l2.next.next = new ListNode(9);
        l2.next.next.next = new ListNode(9);

        // Call the method under test
        Solution sol = new Solution();
        ListNode result = sol.addTwoNumbers(l1, l2);

        // Expected result: [8, 9, 9, 9, 0, 0, 0, 1]
        List<Integer> expected = Arrays.asList(8, 9, 9, 9, 0, 0, 0, 1);

        List<Integer> resultList = new ArrayList<>();
        // Iterate over the result and check each node's value
        while (result != null) {
            resultList.add(result.val);
            result = result.next;
        }

        // Check if the length of the result is as expected
        assertEquals(expected, resultList);
    }

    @Test
    public void testCase1() {
        // Construct l1 = [2, 4, 3]
        ListNode l1 = new ListNode(2);
        l1.next = new ListNode(4);
        l1.next.next = new ListNode(3);

        // Construct l2 = [5, 6, 4]
        ListNode l2 = new ListNode(5);
        l2.next = new ListNode(6);
        l2.next.next = new ListNode(4);

        Solution sol = new Solution();
        ListNode result = sol.addTwoNumbers(l1, l2);

        // Expected result: [7, 0, 8]
        List<Integer> expected = Arrays.asList(7, 0, 8);

        List<Integer> resultList = new ArrayList<>();
        // Iterate over the result and check each node's value
        while (result != null) {
            resultList.add(result.val);
            result = result.next;
        }

        // Check if the length of the result is as expected
        assertEquals(expected, resultList);
    }
}
