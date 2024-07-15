import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLenSubstring = 0;
        for(int a = 0; a < s.length(); a++) {
            HashMap<Character, Integer> charsInString = new HashMap<>();
            int count = 0;
            for(int b = a; b < s.length(); b++) {
                char key = s.charAt(b);
                if(charsInString.containsKey(key)) {
                    break;
                }
                charsInString.put(key, b);
                count++;
            }
            if(count > maxLenSubstring) {
                maxLenSubstring = count;
            }
        }

        return maxLenSubstring;
    }
}