/**
 * 2019-03-26
 * Doit! 자료구조와 함께 배우는 알고리즘 [자바편]
 * 01장 기본 알고리즘, 연습문제 Q12
 * 오른쪽과 같이 위쪽과 왼쪽에 곱하는 수가 있는 곱셈표를 출력하는 프로그램을 작성하세요.
 */
public class Mutilple99 {
    public static void main (String[] args) {
        System.out.println(" | 1  2  3  4  5  6  7  8  9");
        System.out.println("-+---------------------------");

        for (int i=1;i<10;i++) {
            System.out.print(i);
            for (int j=1;j<10;j++) {
                System.out.printf("%3d", i*j);
            }
            System.out.println();
        }
    }
}
