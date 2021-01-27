# 최단경로
import sys
from heapq import heappush, heappop
INF = sys.maxsize

def dijkstra(N, graph, dist, S):
	que = [(0, S)]

	dist[S] = 0
	while(que):
		w, current = heappop(que)

		if dist[current] < w:
			continue

		for nxt, nxt_w in graph[current]:
			nxt_w += w
			if dist[nxt] > nxt_w:
				dist[nxt] = nxt_w
				heappush(que, (nxt_w, nxt))

	

if __name__ == "__main__":
	V, E = map(int, sys.stdin.readline().split())
	K = int(sys.stdin.readline())
	dist = [INF] * V

	graph = [[] for _ in range(V)] 
	for i in range(E):
		u, v, w = map(int, sys.stdin.readline().split())
		graph[u-1].append([v-1, w])

	dijkstra(V, graph, dist, K-1)

	for dis in dist:
		if dis == INF:
			print("INF")
		else:
			print(dis)



