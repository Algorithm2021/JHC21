import sys
from collections import deque, Counter

N = int(sys.stdin.readline())
line = list(map(int,sys.stdin.readline().rstrip().split()))
count, que = Counter(line), deque()
ans = [-1 for i in range(N)]

for i in range(N-1,-1,-1):
	while (que and count[que[-1]]<=count[line[i]]):
 		que.pop()

	if que: ans[i] = que[-1]
	que.append(line[i])

for a in ans:
	print(a, end=' ')