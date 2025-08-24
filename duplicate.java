// Find duplicate element, if duplicate return true 

class Solution {
    public boolean hasDuplicate(int[] nums) {
        for(int i = 0; i < nums.length; i++) {
            for(int j = 0; j < nums.length; j++) {
                if(i != j) {
                    if(nums[i] == nums[j]) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
}

public class duplicate {
    public static void main(String[] argv) {
        int []nums = {1, 2, 3, 1};
        Solution so = new Solution();
        System.out.println(so.hasDuplicate(nums));
    }
}