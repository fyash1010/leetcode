import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Main {
    public static void main() {
    }

    @Test
    public void testCase1() {
        Solution sol = new Solution();
        int out = sol.lengthOfLongestSubstring("abcabcbb");
        assertEquals(3, out);
    }

    @Test
    public void testCase2() {
        Solution sol = new Solution();
        int out = sol.lengthOfLongestSubstring("bbbbb");
        assertEquals(1, out);
    }

    @Test
    public void testCase3() {
        Solution sol = new Solution();
        int out = sol.lengthOfLongestSubstring("pwwkew");
        assertEquals(3, out);
    }
}
