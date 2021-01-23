# K번째 수
import sys

def main():
	N = int(sys.stdin.readline())
	K = int(sys.stdin.readline())


	l, r, ans = 0, K, 0

	while(l<=r):
		mid = int((l + r) / 2)
		count = 0

		for i in range(1, N+1):
			count += min(int(mid / i), N)

		if (count < K):
			l = mid+1
		else:
			ans = mid
			r = mid -1
	print(ans)

if __name__ == '__main__':
	main()