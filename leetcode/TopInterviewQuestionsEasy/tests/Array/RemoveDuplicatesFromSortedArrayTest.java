package Array;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

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
        Assertions.assertEquals(2, RemoveDuplicatesFromSortedArray.solvedByLambda(nums));
    }

    @Test
    void removeDuplicatesFromSortedArrayTest2() {
        int[] nums = new int[]{0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        Assertions.assertEquals(5, RemoveDuplicatesFromSortedArray.solvedByLambda(nums));
    }
}