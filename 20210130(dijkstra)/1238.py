# 파티
import sys
from heapq import heappush, heappop
INF = sys.maxsize

def dijkstra(N, graph, dist, D):
	que = [(0, D)]

	dist[D] = 0
	while(que):
		w, current = heappop(que)

		if dist[current] < w:
			continue

		for nxt, nxt_w in graph[current]:
			nxt_w += w

			if nxt_w < dist[nxt]:
				dist[nxt] = nxt_w
				heappush(que, (nxt_w, nxt))

if __name__ == '__main__':
	N, M, X = map(int, sys.stdin.readline().split())
	T = [[] for _ in range(N)]
	revT = [[] for _ in range(N)]
	dist1, dist2 = [INF] * N, [INF] * N

	for _ in range(M):
		a, b, t = map(int, sys.stdin.readline().split())
		T[a-1].append((b-1, t))
		revT[b-1].append((a-1, t))
	
	dijkstra(N, T, dist1, X-1)
	dijkstra(N, revT, dist2, X-1)

	print(max(sum(i) for i in zip(dist1, dist2)))
