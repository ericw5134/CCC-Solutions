length = int(input()) #length of each array
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))
c = [] #storage of sub-sequence
ci = [] #c's index within list a
cj = [] #c's index within list b FROM LEFT
ck = [] #c's index within list b FROM RIGHT
current = a

suba = []
subb = []

answer = []

#OUTPUT FORMAT:
# direction leftpos rightpos

for i in range(length):
    if b[i] != current:
        c.append(b[i])
        current = b[i]
        cj.append(i)
        if i != 0:
            ck.append(i - 1)
ck.append(len(b)-1)

current = 0
for i in range(len(a)):
    if c[current] == a[i]:
        current += 1
        ci.append(i)

    if current == len(c):
        break

if current != len(c):
    print("NO")
else:
    print("YES")

    for i in range(len(ci)):
        suba = a[cj[i]:ck[i]+1]
        subb = b[cj[i]:ck[i]+1]
        if suba == subb:
            continue
        elif suba[0] == subb[0]:
            answer.append("R " + str(cj[i]) + " " + str(ck[i]))
        elif suba[-1] == subb[-1]:
            answer.append("L " + str(cj[i]) + " " + str(ck[i]))
        else:
            answer.append("R " + str(ci[i]) + " " + str(ck[i]))
            answer.append("L " + str(cj[i]) + " " + str(ci[i]))

    print(len(answer))
    for i in range(len(answer)):
        print(answer[i])