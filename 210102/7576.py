import sys
from collections import deque
w, h = map(int, sys.stdin.readline().split())
graph, q = [], deque()

for i in range(h):
	graph.append(list(map(int, sys.stdin.readline().split())))
	for j in range(len(graph[-1])):
		if (graph[-1][j] == 1): q.append([j, len(graph)-1])

while(q):
	x, y = q.popleft()
	current = graph[y][x]

	if (x-1>=0): 
		if (graph[y][x-1] == 0 or graph[y][x-1]>current+1):
			q.append([x-1,y])
			graph[y][x-1] = current+1
	if (x+1<w): 
		if (graph[y][x+1] == 0 or graph[y][x+1]>current+1):
			q.append([x+1,y])
			graph[y][x+1] = current+1
	if(y-1>=0):
		if (graph[y-1][x] == 0 or graph[y-1][x]>current+1):
			q.append([x,y-1])
			graph[y-1][x] = current+1 
	if(y+1<h):  
		if (graph[y+1][x] == 0 or graph[y+1][x]>current+1):
			q.append([x,y+1])
			graph[y+1][x] = current+1 

for line in graph:
	if 0 in line:
		print('-1'); exit(0)
print(current-1)