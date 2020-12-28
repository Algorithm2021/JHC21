import sys
sys.setrecursionlimit(10**5)
case = int(sys.stdin.readline())

def find_near(graph, width, height, x, y):
	if (field[y][x] == 0): return 0
	field[y][x] = 0
	
	if (y-1 >= 0): find_near(graph, width, height, x, y-1)
	if (y+1 < height): find_near(graph, width, height, x, y+1)
	if (x-1 >= 0): find_near(graph, width, height, x-1, y)
	if (x+1 < width): find_near(graph, width, height, x+1, y)
	
	return 1

for c in range(case):
	width, height, num = map(int, sys.stdin.readline().split())
	field = [[0 for i in range(width)] for j in range(height)]
	count = 0

	for i in range(num):
		x, y = map(int, sys.stdin.readline().split())
		field[y][x] = 1

	for i in range(height):
		for j in range(width):
			count += find_near(field, width, height, j, i)
	print(count)