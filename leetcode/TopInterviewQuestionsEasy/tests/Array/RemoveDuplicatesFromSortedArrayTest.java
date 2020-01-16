package Array;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.List;

class RemoveDuplicatesFromSortedArrayTest {

    @Test
    void removeDuplicatesFromSortedArrayTest3() {
        int[] nums = new int[]{1, 1, 2};
        Assertions.assertEquals(2, RemoveDuplicatesFromSortedArray.solution(nums));
    }

    @Test
    void removeDuplicatesFromSortedArrayTest4() {
        int[] nums = new int[]{0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        Assertions.assertEquals(5, RemoveDuplicatesFromSortedArray.solution(nums));
    }

    @Test
    void removeDuplicatesFromSortedArrayTest1() {
        int[] nums = new int[]{1, 1, 2};
        List<Integer> answerNums = Arrays.asList(1, 2);

        List<Integer> result = RemoveDuplicatesFromSortedArray.solvedByLambda(nums);

        Assertions.assertEquals(2, result.size());
        Assertions.assertEquals(answerNums, result);
    }

    @Test
    void removeDuplicatesFromSortedArrayTest2() {
        int[] nums = new int[]{0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        List<Integer> answerNums = Arrays.asList(0, 1, 2, 3, 4);

        List<Integer> result = RemoveDuplicatesFromSortedArray.solvedByLambda(nums);

        Assertions.assertEquals(5, result.size());
        Assertions.assertEquals(answerNums, result);
    }
}