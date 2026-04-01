"""
https://dmoj.ca/problem/ccc21j4
"""

books = input()

l_end = books.count('L')            # index of where Ls should end 
m_end = l_end + books.count('M')    # index of where Ms should end 

l_sec, m_sec, s_sec = books[:l_end], books[l_end:m_end], books[m_end:]  # l's section in books, m's section ... 

# calculate the result, which is the sum of:
# The count of 'M' and 'S' books before the first 'M'.
# The maximum count of either 'S' books in the 'M' segment or 'M' books in the 'S' segment 
print(l_sec.count('M') + l_sec.count('S') + max(m_sec.count('S'), s_sec.count('M')))