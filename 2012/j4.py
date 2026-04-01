"""
https://dmoj.ca/problem/ccc12j4
"""


import string

k, word = int(input()), input()


def get_decode(char, idx):
    new = ord(char) + 3 * (idx + 1) + k
    new = 65 + (new - 91) if new > 90 else new
    return chr(new)


for idx in range(len(word)):
    for char in string.ascii_uppercase:
        if get_decode(char, idx) == word[idx]:
            print(char, end='')
            break
print()