/**
 * https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
 */
package Array;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class RemoveDuplicatesFromSortedArray {
    public static List<Integer> solvedByLambda(int[] nums) {
        return Arrays.stream(nums).distinct().boxed().collect(Collectors.toList());
    }

    public static int solution(int[] nums) {
        int count = 1;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] != nums[i + 1]) {
                nums[count] = nums[i + 1];
                count++;
            }
        }
        return count;
    }

    public static int leetcodeSolution(int[] nums) {
        if (nums.length == 0) return 0;
        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[j] != nums[i]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }
}
