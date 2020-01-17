package chap01;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class Max3Test {

    @Test
    void main() {
        int[] nums = new int[]{1, 4, 2};
        assertEquals(4, Max3.main(nums));
    }
}