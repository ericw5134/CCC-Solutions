import java.util.Scanner;

public class s1 {
    public static double area(double a, double b, double h) {
        return h * ((a + b) / 2.0);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        double[] heights = new double[N + 1];
        double[] widths = new double[N];

        for (int i = 0; i <= N; i++) {
            heights[i] = scanner.nextDouble();
        }

        for (int i = 0; i < N; i++) {
            widths[i] = scanner.nextDouble();
        }

        double totalArea = 0;
        for (int i = 0; i < N; i++) {
            totalArea += area(heights[i], heights[i + 1], widths[i]);
        }

        System.out.println(totalArea);
        scanner.close();
    }
}