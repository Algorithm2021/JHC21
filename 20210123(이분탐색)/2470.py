# 두 용액
import sys

def main():
	N = int(sys.stdin.readline())
	arr = list(map(int, sys.stdin.readline().split()))
	arr.sort()

	a, b = 0, len(arr)-1
	tmp_a, tmp_b, mini = a, b, arr[0] + arr[-1]
	
	
	while(a < b):
		tmp = arr[a] + arr[b]

		if abs(tmp) <= abs(mini):
			mini = tmp
			tmp_a = a
			tmp_b = b

		if tmp > 0: b-=1
		else: a+=1

	print(arr[tmp_a], arr[tmp_b])

if __name__ == '__main__':
	main()