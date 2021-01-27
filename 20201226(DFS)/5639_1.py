import sys
sys.setrecursionlimit(10**5)

def postOrder(start, end):
	if (start > end): return

	div = end+1
	for i in range(start+1, end+1):
		if nodes[start] < nodes[i]:
			div = i
			break

	postOrder(start+1, div-1)
	postOrder(div, end)
	print(nodes[start])

nodes = []

while(1):
	try: v = int(sys.stdin.readline())
	except: break
	nodes.append(v)
	
postOrder(0, len(nodes)-1)
