'''
https://dmoj.ca/problem/ccc23j5

note:
1. use DFS / BFS, although DFS should be more logical in the context of the question..
2. the turning mechanism is kind of tricky..
  - at places where we can still turn, we should also add the turned states into our stack, kinda like BFS in a sense
'''

# Inputs
word = input()
rows = int(input())
cols = int(input())

grid = []

for i in range(rows):
  grid.append(input().split())

class State:
  def __init__(self, r, c, dr, dc, idx, turned):
    self.r = r      # current row position
    self.c = c      # current column position
    self.dr = dr    # row direction of movement
    self.dc = dc    # column direction of movement
    self.idx = idx  # index of the character in the word being matched
    self.turned = turned  # bool: has direction changed? note we only change direction once! 

todo = [] # stack for DFS

# Starting positions:
for i in range(rows):
  for j in range(cols):
    if grid[i][j] == word[0]: # if we find the 1st letter in word
      # 8 initial direction
      todo.append(State(i, j, 0, 1, 0, False))   # right

      todo.append(State(i, j, -1, 1, 0, False))  # up right
      todo.append(State(i, j, -1, 0, 0, False))  # up
      todo.append(State(i, j, -1, -1, 0, False)) # up left

      todo.append(State(i, j, 0, -1, 0, False))  # left
      
      todo.append(State(i, j, 1, -1, 0, False))  # down left
      todo.append(State(i, j, 1, 0, 0, False))   # down
      todo.append(State(i, j, 1, 1, 0, False))   # down right

ans = 0

while len(todo) > 0:

  cur = todo.pop()  # pop state from stack

  if not ((0 <= cur.r < rows) and (0 <= cur.c < cols)): # check for boundaries
    continue  # skip if out of bounds

  if grid[cur.r][cur.c] != word[cur.idx]: # check if the letter match
    continue  # skip if character doesn't match expected letter

  if cur.idx == len(word) - 1:  # check for solution (checked every letter)
    ans += 1
    continue

  # go to the next position in the same direction
  nextState = State(cur.r + cur.dr, cur.c + cur.dc, cur.dr, cur.dc, cur.idx + 1, cur.turned)
  todo.append(nextState)

  if not cur.turned and cur.idx < len(word) - 2:  # if we havent turned yet AND we can only turn if there are still 2+ characters away from finishing the check
    
    if cur.dr == 0: # if we are moving horizontally
      todo.append(State(cur.r + cur.dr, cur.c + cur.dc, 1, 0, cur.idx + 1, True)) # then go down instead
      todo.append(State(cur.r + cur.dr, cur.c + cur.dc, -1, 0, cur.idx + 1, True))  # then go up instead
    
    elif cur.dc == 0: # if we are moving vertically
      todo.append(State(cur.r + cur.dr, cur.c + cur.dc, 0, 1, cur.idx + 1, True)) # then go right instead
      todo.append(State(cur.r + cur.dr, cur.c + cur.dc, 0, -1, cur.idx + 1, True))  # then go left instead
    
    else: # if we are moving diagonally
      todo.append(State(cur.r + cur.dr, cur.c + cur.dc, -cur.dr, cur.dc, cur.idx + 1, True))  # flip row movement
      todo.append(State(cur.r + cur.dr, cur.c + cur.dc, cur.dr, -cur.dc, cur.idx + 1, True))  # flip column movement    
  
print(ans)

