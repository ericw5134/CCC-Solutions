import math, sys

input = sys.stdin.readline  # fast input

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numberOfTests = int(input())

testCases = []
for _ in range(numberOfTests):
    testCases.append(int(input()))

for test in testCases:
    for i in range(2, 2 * test):
        j = 2 * test - i
        if is_prime(i) and is_prime(j):
            print(f"{i} {j}")
            break

'''
import math

# Generate all prime numbers up to max_n using Sieve of Eratosthenes
def eratosthenes(max_n):
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(max_n)) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False
    return [i for i, is_p in enumerate(sieve) if is_p]

# Input
numberOfTests = int(input())
testCases = [int(input()) for _ in range(numberOfTests)]

# Precompute primes up to the largest 2 * test value
max_value = max(testCases) * 2
primes = eratosthenes(max_value)
prime_set = set(primes)  # For O(1) lookup

# Solve each test case
for test in testCases:
    target = 2 * test
    for p in primes:
        if p > target:
            break
        if (target - p) in prime_set:
            print(f"{p} {target - p}")
            break
'''