class State():
    def __init__(self, row, column, total):
        self.row = row
        self.column = column
        self.total = total

R = int(input())
C = int(input())
maximumTileCost = int(input())

grid = []
count = 1

for j in range(R):
    buildr = []
    for i in range(C):
        buildr.append(count)
        if count >= maximumTileCost:
            count = 1
        else:
            count += 1
    grid.append(buildr)

totalCost = 0

todo = []
visited = []

lowestTotal = 999999999999

for i in range(C):
    todo.append(State(0, i, 0))
    while todo:
        cur = todo.pop()
        cur.total = cur.total + grid[cur.row][cur.column]
        visited.append(cur)
        
        if cur.row == R-1:
            if cur.total < lowestTotal:
                lowestTotal = cur.total
            continue
        if 0 <= cur.column - 1 < C:
            todo.append(State(cur.row+1, cur.column-1, cur.total))
        if 0 <= cur.column + 1 < C:
            todo.append(State(cur.row+1, cur.column+1, cur.total))
        todo.append(State(cur.row+1, cur.column, cur.total))

print(lowestTotal)