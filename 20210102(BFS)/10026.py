import sys
sys.setrecursionlimit(10**5)

def check_color(graph, n, x, y, prev, check = 'X'):
	if (graph[x][y] ==  prev):
		graph[x][y] = check
		if (y-1 >= 0): check_color(graph, n, x, y-1, prev, check)
		if (y+1 < n): check_color(graph, n, x, y+1, prev, check)
		if (x-1 >= 0): check_color(graph, n, x-1, y, prev, check)
		if (x+1 < n): check_color(graph, n, x+1, y, prev, check)
	return 1

n = int(sys.stdin.readline())
graph, r, g, b, rg = [], 0, 0, 0, 0

for i in range(n):
	graph.append(list(sys.stdin.readline().rstrip()))

for i in range(n):
	for j in range(n):
		if (graph[i][j] == 'R'):
			r+=check_color(graph, n, i, j, 'R')
		elif (graph[i][j] == 'G'):
			g+=check_color(graph, n, i, j, 'G')

for i in range(n):
	for j in range(n):
		if (graph[i][j] == 'B'):
			b+=check_color(graph, n, i, j, 'B', check = 'O')
		elif (graph[i][j] == 'X'):
			rg+=check_color(graph, n, i, j, 'X', check = 'O')

print((r+g+b), (b+rg))