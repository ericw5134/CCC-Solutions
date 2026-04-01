'''
https://dmoj.ca/problem/ccc23s2

note:
1. use the sliding window techanique
2. write a DP algorithm, good practice
3. PyPy 3 runs fine (more memory used), but Python 3 TLEs, probably should be done using C++ or another faster language
'''

n = int(input())
h = list(map(int, input().split()))
pre = [[0] * (n + 1) for _ in range(n + 1)] # stores the computed value for a subsequence starting at index i and ending at index j

# calculate for all window sizes
for i in range(1, n + 1):
    l, r = 0, i - 1  # adjusted to 0-based indexing
    best = float('inf')
    while r < n:
        pre[l][r] = abs(h[l] - h[r]) + (pre[l + 1][r - 1] if l + 1 <= r - 1 else 0) # The absolute difference between the first and last element of the 
                                                                                    # window is added to the precomputed value of the inner subarray
                                                                                    # if l+1 > r-1, then substitude with 0
        best = min(best, pre[l][r]) # keep track of minimum pre[l][r]
        l += 1
        r += 1
    print(best, end=' ' if i != n else '\n')
