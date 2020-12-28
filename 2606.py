n = int(input())
m = int(input())
graph, corr = dict(), [False for i in range(n)]

def search(v):
	corr[int(v)-1] = True
	for e in graph[v]:
		if not corr[int(e)-1]:
			search(e)
		
		
for i in range(m):
	a, b = input().split()
	if (a) in graph: graph[a].append(b)
	else: graph[a] = [b]
	if (b) in graph: graph[b].append(a)
	else: graph[b] = [a]

search('1')

print(sum(corr)-1)
