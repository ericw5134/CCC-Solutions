import math

first_line = list(map(int, input().split()))

N = first_line[0]
c = first_line[1:]

while len(c) < N:
    c += list(map(int, input().split()))

# unknown subtask
if all(v == -1 for v in c):
    # N is 1e5 here
    K = 100
    block = N // K

    guesses = []

    for g in range(K):
        start = g * block + 1
        end = (g + 1) * block if g < K - 1 else N

        inds = list(range(start, end + 1))

        if len(inds) < 2:
            break

        mid = len(inds) // 2

        A = inds[:mid]
        B = inds[mid:]

        if not A:
            A = [B.pop()]

        if not B:
            B = [A.pop()]

        guesses.append((A, B))

    print(len(guesses))

    for A, B in guesses:
        print(len(A), len(B))
        print(" ".join(map(str, A)))
        print(" ".join(map(str, B)))

else:
    # known values
    if N <= 3:
        idxs = list(range(1, N + 1))
        found = None

        for amask in range(1, (1 << N) - 1):
            A = []

            for i in range(N):
                if (amask >> i) & 1:
                    A.append(idxs[i])

            rem = []

            for i in range(N):
                if not ((amask >> i) & 1):
                    rem.append(idxs[i])

            if not rem:
                continue

            suma = 0

            for i in A:
                suma += c[i - 1]

            rlen = len(rem)

            for bmask in range(1, 1 << rlen):
                B = []

                for i in range(rlen):
                    if (bmask >> i) & 1:
                        B.append(rem[i])

                sumb = 0

                for i in B:
                    sumb += c[i - 1]

                if math.gcd(suma, sumb) > 1:
                    found = (A, B)
                    break

            if found:
                break

        if not found:
            print("NO")
        else:
            A, B = found

            print("YES")
            print(len(A), len(B))
            print(" ".join(map(str, A)))
            print(" ".join(map(str, B)))

    else:
        evens = []
        odds = []

        for i in range(N):
            if c[i] % 2 == 0:
                evens.append(i + 1)
            else:
                odds.append(i + 1)

        if len(evens) >= 2:
            A = [evens[0]]
            B = [evens[1]]

        elif len(evens) == 1:
            A = [evens[0]]
            B = [odds[0], odds[1]]

        else:
            A = [odds[0], odds[1]]
            B = [odds[2], odds[3]]

        print("YES")
        print(len(A), len(B))
        print(" ".join(map(str, A)))
        print(" ".join(map(str, B)))