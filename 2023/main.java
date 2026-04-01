import java.util.*;

class State {
    int r, c, dr, dc, idx;
    boolean turned;

    State(int r, int c, int dr, int dc, int idx, boolean turned) {
        this.r = r;
        this.c = c;
        this.dr = dr;
        this.dc = dc;
        this.idx = idx;
        this.turned = turned;
    }
}

public class WordSearch {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        String word = scanner.nextLine();
        int rows = scanner.nextInt();
        int cols = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        
        String[][] grid = new String[rows][cols];
        for (int i = 0; i < rows; i++) {
            grid[i] = scanner.nextLine().split(" ");
        }
        
        scanner.close();
        
        Stack<State> todo = new Stack<>();
        
        // Starting positions
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j].equals(word.substring(0, 1))) {
                    // 8 initial directions
                    todo.push(new State(i, j, 0, 1, 0, false));  // right
                    todo.push(new State(i, j, -1, 1, 0, false)); // up-right
                    todo.push(new State(i, j, -1, 0, 0, false)); // up
                    todo.push(new State(i, j, -1, -1, 0, false)); // up-left
                    todo.push(new State(i, j, 0, -1, 0, false)); // left
                    todo.push(new State(i, j, 1, -1, 0, false)); // down-left
                    todo.push(new State(i, j, 1, 0, 0, false)); // down
                    todo.push(new State(i, j, 1, 1, 0, false)); // down-right
                }
            }
        }
        
        int ans = 0;
        
        while (!todo.isEmpty()) {
            State cur = todo.pop();
            
            if (cur.r < 0 || cur.r >= rows || cur.c < 0 || cur.c >= cols) {
                continue; // Out of bounds
            }
            
            if (!grid[cur.r][cur.c].equals(word.substring(cur.idx, cur.idx + 1))) {
                continue; // Character mismatch
            }
            
            if (cur.idx == word.length() - 1) {
                ans++;
                continue;
            }
            
            // Move in the same direction
            todo.push(new State(cur.r + cur.dr, cur.c + cur.dc, cur.dr, cur.dc, cur.idx + 1, cur.turned));
            
            if (!cur.turned && cur.idx < word.length() - 2) {
                // Allow one turn
                if (cur.dr == 0) { // Moving horizontally
                    todo.push(new State(cur.r + cur.dr, cur.c + cur.dc, 1, 0, cur.idx + 1, true)); // Down
                    todo.push(new State(cur.r + cur.dr, cur.c + cur.dc, -1, 0, cur.idx + 1, true)); // Up
                } else if (cur.dc == 0) { // Moving vertically
                    todo.push(new State(cur.r + cur.dr, cur.c + cur.dc, 0, 1, cur.idx + 1, true)); // Right
                    todo.push(new State(cur.r + cur.dr, cur.c + cur.dc, 0, -1, cur.idx + 1, true)); // Left
                } else { // Moving diagonally
                    todo.push(new State(cur.r + cur.dr, cur.c + cur.dc, -cur.dr, cur.dc, cur.idx + 1, true)); // Flip row movement
                    todo.push(new State(cur.r + cur.dr, cur.c + cur.dc, cur.dr, -cur.dc, cur.idx + 1, true)); // Flip column movement
                }
            }
        }
        
        System.out.println(ans);
    }
}
