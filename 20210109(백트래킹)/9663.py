import sys
from collections import deque

N = int(sys.stdin.readline())
c = 0

def find_queens(n, queens):
	global c

	if len(queens) == n: 
		c += 1
		return
	
	corr = list(range(n))
	for idx in range(len(queens)):
		if queens[idx] in corr: 
			corr.remove(queens[idx])
		
		dist = len(queens) - idx

		if queens[idx] + dist in corr:
			corr.remove(queens[idx] + dist)			
		if queens[idx] - dist in corr:
			corr.remove(queens[idx] - dist)

	for co in corr:
		find_queens(n, queens+[co])

	return

for i in range(N):
	find_queens(N, [i])

print(c)
