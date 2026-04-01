def func(seq):
    left = 0
    q_count = 0
    max_length = 0

    for right in range(len(seq)):
        if seq[right] == 'q':
            q_count += 1

        while q_count > 1:
            if seq[left] == 'q':
                q_count -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

N = int(input())
days = [input() for _ in range(N)]

print(func(days))
