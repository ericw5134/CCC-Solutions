'''
https://dmoj.ca/problem/ccc17s3
'''

# constants
MAXN = 2001

# input variables
L = [0] * MAXN  # frequency of boards of each length
F = [0] * (MAXN * 2 - 1)  # frequency of total lengths formed by pairs

# function to count pairs
def cnt():
    for n in range(1, 2001):
        if L[n]:
            # case 1: Two boards of the same length
            if L[n] > 1:
                F[n * 2] += L[n] // 2
            # case 2: Two boards of different lengths
            for s in range(n + 1, 2001):
                if L[s]:
                    F[n + s] += min(L[n], L[s])

# function to find the maximum number of pairs and their count
def search():
    global maxl, nmax
    for i in range(1, 4001):
        if F[i] > maxl:
            maxl = F[i]
            nmax = 1
        elif F[i] == maxl:
            nmax += 1

N = int(input())  # number of boards
numbers = list(map(int, input().split()))
for num in numbers:
    L[num] += 1

maxl, nmax = 0, 1  # initialize max pairs and distinct lengths
cnt()  # count the pairs
search()  # find the maximum pairs and their counts

print(maxl, nmax)
