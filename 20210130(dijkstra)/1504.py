# 특정한 최단 경로
import sys
from heapq import heappush, heappop
INF = sys.maxsize

def dijkstra(N, graph, S):
	dist = [INF] * N
	que = [(0, S)]
	dist[S] = 0

	while(que):
		w, current = heappop(que)

		if dist[current] < w:
			continue

		for nxt, nxt_w in graph[current]:
			nxt_w += w
			if nxt_w < dist[nxt]:
				dist[nxt] = nxt_w
				heappush(que, (nxt_w, nxt))
	return dist

def main():
	N, E = map(int, sys.stdin.readline().split())
	graph = [[] for _ in range(N)]

	for _ in range(E):
		a, b, c = map(int, sys.stdin.readline().split())
		graph[a-1].append((b-1, c))
		graph[b-1].append((a-1, c))
	V1, V2 = map(int, sys.stdin.readline().split())
	
	v1_dist = dijkstra(N, graph, V1-1)
	v2_dist = dijkstra(N, graph, V2-1)

	if v1_dist[V2-1] == INF or v1_dist[N-1] == INF:
		print('-1'); return 0

	if v2_dist[N-1] == INF:
		print('-1'); return 0

	tmp1 = v1_dist[0] + v1_dist[V2-1] + v2_dist[N-1]
	tmp2 = v2_dist[0] + v1_dist[N-1] + v2_dist[V1-1]

	print(min(tmp1, tmp2))

if __name__ == '__main__':
	main()