"""
https://dmoj.ca/problem/ccc18j3

Note:
1. array slicing is useful for this question
"""

distances = [int(i) for i in input().split()]

for i in range(5):
    val = 0 # val keeps track of the accumlated distance we travelled
    output = []

    # find the distances before given city
    for distance in distances[:i][::-1]:
        val += distance
        output.append(val)
    output.reverse()

    val = 0 # reset val

    # find the distances after given city
    for distance in distances[i:]:
        val += distance
        output.append(val)
    output.insert(i, 0)
    print(' '.join(str(i) for i in output))


'''
OR if you are lazy (or smart in a sense):

q = list(map(int, input().split()))
print("0",q[0],q[0]+q[1],q[0]+q[1]+q[2],q[0]+q[1]+q[2]+q[3])
print(q[0],"0",q[1],q[1]+q[2],q[1]+q[2]+q[3])
print(q[0]+q[1],q[1],"0",q[2],q[2]+q[3])
print(q[0]+q[1]+q[2],q[1]+q[2],q[2],"0",q[3])
print(q[0]+q[1]+q[2]+q[3],q[1]+q[2]+q[3],q[2]+q[3],q[3],"0")

works too, gets you full marks
'''

