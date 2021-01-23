# 3020 개똥벌래
import sys

def loc(arr, b):
	l, r = 0, len(arr)-1

	while(l<=r):
		div = int((l+r)/2)

		if arr[div] <= b:
			l = div+1
		else:
			r = div-1
	return len(arr) - (r + 1)

def main():
	N, H = map(int, sys.stdin.readline().split())
	upper, lower = [], []
	ans, cnt = 200000, 0

	for i in range(N):
		sta = int(sys.stdin.readline())
		if i%2: lower.append(sta)
		else: upper.append(sta)

	lower.sort()
	upper.sort()

	for i in range(H):
		tmp = loc(lower, i) + loc(upper, H-(i+1)) 
		if ans == tmp: cnt+=1
		elif ans > tmp:
			cnt = 1; ans = tmp
	print(ans, cnt)

if __name__ == '__main__':
	main()
