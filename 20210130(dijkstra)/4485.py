# 녹색 옷 입은 애가 젤다지?
import sys
from heapq import heappush, heappop
INF = sys.maxsize

def dijkstra(N, graph):
	que = [(graph[0][0], (0,0))]
	dist = [[INF for _ in range(N)] for _ in range(N)]
	dist[0][0] = graph[0][0]

	while(que):
		w, (x, y) = heappop(que)

		if dist[x][y] < w:
			continue

		nxt = []
		if x-1 >= 0:
			nxt.append((x-1,y))
		if x+1 < N:
			nxt.append((x+1, y))
		if y-1 >= 0:
			nxt.append((x, y-1))
		if y+1 < N:
			nxt.append((x, y+1))

		for nx, ny in nxt:
			nxt_w = graph[nx][ny] + w

			if nxt_w < dist[nx][ny]:
				dist[nx][ny] = nxt_w
				heappush(que, (nxt_w, (nx, ny)))

	return dist[N-1][N-1]

def main():
	idx = 1
	while(True):
		N = int(sys.stdin.readline())
		if not N: return 0

		field = []
		for i in range(N):
			field.append(list(map(int,sys.stdin.readline().split())))

		print("Problem ", idx, ": ", dijkstra(N, field), sep='')
		idx+=1

if __name__ == '__main__':
	main()