'''
https://dmoj.ca/problem/ccc21s2
'''

def count_golden_cells(M, N, K, operations):
    row_operations = [0] * M
    column_operations = [0] * N

    for operation in operations:
        type, index = operation.split()
        index = int(index) - 1
        if type == 'R':
            row_operations[index] += 1
        elif type == 'C':
            column_operations[index] += 1

    golden_cells = 0
    for i in range(M):
        for j in range(N):
            if (row_operations[i] + column_operations[j]) % 2 == 1:
                golden_cells += 1

    return golden_cells

M, N, K = int(input()), int(input()), int(input())
operations = [input() for _ in range(K)]

result = count_golden_cells(M, N, K, operations)
print(result)
