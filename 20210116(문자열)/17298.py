import sys

N = int(sys.stdin.readline())
line = list(map(int,sys.stdin.readline().rstrip().split()))
ans, que = [-1]*(N), [line[-1]]

for i in range(N-2, -1, -1):
	if line[i] < que[-1]:
		ans[i] = que[-1]
	else:
		while(que and line[i] >= que[-1]):
			que.pop()
		if (que):
			ans[i] = que[-1]
	que.append(line[i])

for a in ans:
	print(a, end=' ')
