import sys

'''
import sys

# read the number of elements
n = int(sys.stdin.readline())

# reading a list of integers on the next line
# 10 20 30 40 -> [10, 20, 30, 40]
data = list(map(int, sys.stdin.readline().split()))
'''

def solve():
    n = int(sys.stdin.readline())
    
    balls = list(map(int, sys.stdin.readline().split()))
    
    # prefix sums array for O(1) range sum calculation
    # each index ps[i] stores the sum of all elements from the start 
    # of the array up to (but not including) index i
    ps = [0] * (n + 1)
    for i in range(n):
        ps[i+1] = ps[i] + balls[i]
    
    # dp[i][j] is True if range [i, j] can be merged
    dp = [[False] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = True     # base case: any range of length 1 is true
    
    # track the largest riceball seen so far
    max_val = max(balls)

    for length in range(2, n + 1):  # try solving length 2, 3, ...
        for i in range(n - length + 1):     # the start of our current range
            j = i + length - 1  # the end of our current range
            l, r = i, j     # two pointer 
            
            while l < r:
                sum_l = ps[l+1] - ps[i]     # weigth of the left group
                sum_r = ps[j+1] - ps[r]     # weight of the right group
                
                if sum_l < sum_r:
                    l += 1  # left is too light, add more riceballs to it
                elif sum_l > sum_r:
                    r -= 1  # right is too light, add more riceballs to it
                else:
                    # if sum_l == sum_r, check if the parts are combinable.
                    # Case 1: two parts (no middle). Check if dp[i][l] and dp[r][j] are True.
                    # Case 2: three parts. Check if dp[i][l], dp[r][j], AND middle dp[l+1][r-1] are True.
                    if dp[i][l] and dp[r][j]:
                        if l + 1 == r or dp[l+1][r-1]:
                            dp[i][j] = True
                            max_val = max(max_val, ps[j+1] - ps[i])
                            break   # found a way to merge
                    l += 1
                    
    print(max_val)

solve()