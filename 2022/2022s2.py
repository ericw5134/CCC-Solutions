"""
https://dmoj.ca/problem/ccc22s2
"""

must, must_not = {}, {}
for rules in (must, must_not):
    for _ in range(int(input())):
        s1, s2 = input().split()
        if s1 not in rules:
            rules[s1] = [s2]
        else:
            rules[s1].append(s2)

violations = 0
for _ in range(int(input())):
    group = set(input().split())
    for i in group:
        violations += sum(1 for mi in must.get(i, []) if mi not in group) + \
            sum(1 for mni in must_not.get(i, []) if mni in group)

print(violations)