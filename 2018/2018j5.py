'''
https://dmoj.ca/problem/ccc18j5

note:
1. use BFS algorithm
'''

from queue import Queue

'''
a hash map of the following property:
- key are page numbers
- value are the pages that can be reached from key
'''
book = {}

# construct book with all pages
numberOfPages = int(input())
for pageNumber in range(numberOfPages):
    num_paths, *destinations = input().split()   # * makes destinations collect all remaining inputs other than the 1st
    if int(num_paths) == 0:
        book[pageNumber + 1] = [0]  
    else:
        book[pageNumber + 1] = [int(i) for i in destinations]

# we are going to use BFS to find all paths
Q = Queue()
Q.put([1])      # start at page 1 in BFS

reached = {1}   # keep track of pages visited
valid = []      # store valid paths

while Q.qsize() > 0:       # while Q is not empty
    path = Q.get()         # get a path from the head of the Q
    for rechablesPage in book[path[-1]]: # retrieves the destinations stored in the book dictionary 
                                         # corresponding to the last page in the current path
        if rechablesPage == 0:      # if next reachable page is 0, that mean we are at end page, add it to valid
            valid.append(path)  
        elif rechablesPage not in reached:  # if not yet reached, add it to reached
            reached.add(rechablesPage)
            Q.put(path + [rechablesPage])

if len(reached) == len(book):
    print("Y")
else:
    print("N")
    
print(len(valid[0]))

