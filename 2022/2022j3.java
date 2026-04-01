import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();

        String letters = "";
        char sign = ' ';
        String number = "";

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);

            if (Character.isUpperCase(c)) { // a letter
                // if we already collected a full instruction, print it
                if (!letters.isEmpty() && !number.isEmpty()) {
                    System.out.println(letters + " " + (sign == '+' ? "tighten" : "loosen") + " " + number);
                    letters = "";
                    number = "";
                }
                letters += c;
            } else if (c == '+' || c == '-') {  // a sign
                sign = c;
            } else { // a digit
                number += c;
            }
        }

        // Print the last instruction
        if (!letters.isEmpty() && !number.isEmpty()) {
            System.out.println(letters + " " + (sign == '+' ? "tighten" : "loosen") + " " + number);
        }
    }
}
