import sys

data = list(map(int, sys.stdin.buffer.read().split()))

N = data[0]
K = data[1]
A = data[2:]

MAXV = max(A) + 2

tree = [0] * (MAXV + 2)

def add(i, x):
    while i < len(tree):
        tree[i] += x
        i += i & -i

def query(i):
    total = 0
    while i > 0:
        total += tree[i]
        i -= i & -i
    return total

zero_before = [0] * N
count_zero = 0

for i in range(N):
    zero_before[i] = count_zero

    if A[i] == 0:
        count_zero += 1

total_zeros = count_zero

constraints = []

for i in range(N - 1, -1, -1):
    v = A[i]

    if v == 0:
        continue

    fixed_smaller = query(v - 1)
    zeros_right = total_zeros - zero_before[i]

    constraints.append((v, fixed_smaller, zeros_right))

    add(v, 1)

constraints.sort(reverse=True)

def possible(capacity):
    cost = 0
    raised_zeros = 0

    for v, fixed_smaller, zeros_right in constraints:
        if fixed_smaller > capacity:
            return False

        need_raised = zeros_right + fixed_smaller - capacity

        if need_raised > raised_zeros:
            extra = need_raised - raised_zeros
            cost += extra * v

            if cost > K:
                return False

            raised_zeros = need_raised

    return True

low = 0
high = N - 1

while low < high:
    mid = (low + high) // 2

    if possible(mid):
        high = mid
    else:
        low = mid + 1

print(low)