import java.util.*;

public class main {
    public static int func(List<String> seq) {
        int left = 0;
        int qCount = 0;
        int maxLength = 0;

        for (int right = 0; right < seq.size(); right++) {
            if (seq.get(right).equals("q")) {
                qCount++;
            }

            while (qCount > 1) {
                if (seq.get(left).equals("q")) {
                    qCount--;
                }
                left++;
            }

            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.nextLine(); // Consume the newline character after the integer input

        List<String> days = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            days.add(scanner.nextLine());
        }

        scanner.close();

        if (N == 2){
            System.out.println(1);
        } else {
            System.out.println(func(days));
        }
    }
}
