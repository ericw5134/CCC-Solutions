"""
https://dmoj.ca/problem/ccc18j1
"""

# if 1st == 8 or 9 AND 2nd == 3rd AND 4th == 8 or 9
if (input() in ('8', '9') and input() == input() and input() in ('8', '9')):
    print("ignore")
else:
    print("answer")