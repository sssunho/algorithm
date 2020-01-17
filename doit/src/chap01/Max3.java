package chap01;

import java.util.Scanner;

public class Max3 {
    public static int main(int[] nums) {
        // max에 첫번째 값을 넣는다
        int max = nums[0];

        for (int num : nums) {
            // num이 max보다 크면 max의 값을 num으로 바꾼다.
            if (max < num) max = num;
        }
        return max;
    }
}