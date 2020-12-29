import sys
from collections import deque
sys.setrecursionlimit(10**5)
N, M, V = map(int,input().split())
graph = [[] for i in range(N)]
checked = [False for i in range(N)]
que = deque()

for i in range(M):
	a, b = map(int, input().split())
	graph[a-1].append(b)
	graph[b-1].append(a)

for e in graph:
	e.sort()

def dfs_search(v):
	checked[v-1] = True
	print(v, end=' ')

	for e in graph[v-1]: 
		if not checked[e-1]: dfs_search(e)

def bfs_search(v):
	bfs_checked = [False for i in range(N)]
	que.append(v)

	while(que):
		cur = que.popleft()
		if not bfs_checked[cur-1]: print(cur, end=' ')
		bfs_checked[cur-1] = True
		
		for e in graph[cur-1]: 
			if not bfs_checked[e-1]: que.append(e)

dfs_search(V)
print('')
bfs_search(V)