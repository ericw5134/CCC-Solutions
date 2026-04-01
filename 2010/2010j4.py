'''
** all cycles start at the first digit **
'''

all_diff = [] 

while True:
    sequence = list(map(int, input().split())) 
    if sequence[0] == 0:  
        break
    diff = []  # diff[i] = temperature[i+1] - temperature[i]
    for i in range(2, len(sequence), 1):
        diff.append(sequence[i] - sequence[i-1])
    all_diff.append(diff)  # save this case's differences


for sublist in all_diff:    
    m = len(sublist)            # number of differences (n - 1)
    if m == 0:                  # if there was only 1 temperature, there are no differences
        print(0)
        continue
    found = False
    # try every possible cycle length from 1 up to m.
    # we want the SMALLEST cycle length that can generate the whole diff list.
    for cycle in range(1, m + 1):
        ok = True
        # check if the diff list repeats every "cycle" steps.
        # that means: sublist[i] must equal the pattern element sublist[i % cycle]
        # for all i in [0, m-1]. (The last repetition can be cut off automatically.)
        for i in range(m):
            if sublist[i] != sublist[i % cycle]:
                ok = False      # cycle length doesn't work
                break
        if ok:
            # found the smallest valid cycle length
            print(cycle)
            found = True
            break
    # this is basically never needed because cycle = m always works,
    # but it's here as a safe fallback.
    if not found:
        print(m)
