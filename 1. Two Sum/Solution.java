import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int a = 0; a < nums.length; a++) {
            if(map.get(nums[a]) == null) {
                map.put(target - nums[a], a);
            } else {
                int[] out = {a, map.get(nums[a])};
                return out;
            }
        }

        int[] defaultOut = {0, 0};
        return defaultOut;
    }
}