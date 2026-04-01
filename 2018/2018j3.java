package 2018;

public class 2018j3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] q = new int[4];
        for (int i = 0; i < 4; i++) {
            q[i] = scanner.nextInt();
        }
        System.out.println("0 " + q[0] + " " + (q[0] + q[1]) + " " + (q[0] + q[1] + q[2]) + " " + (q[0] + q[1] + q[2] + q[3]));
        System.out.println(q[0] + " 0 " + q[1] + " " + (q[1] + q[2]) + " " + (q[1] + q[2] + q[3]));
        System.out.println((q[0] + q[1]) + " " + q[1] + " 0 " + q[2] + " " + (q[2] + q[3]));
        System.out.println((q[0] + q[1] + q[2]) + " " + (q[1] + q[2]) + " " + q[2] + " 0 " + q[3]);
        System.out.println((q[0] + q[1] + q[2] + q[3]) + " " + (q[1] + q[2] + q[3]) + " " + (q[2] + q[3]) + " " + q[3] + " 0");
    }
}
