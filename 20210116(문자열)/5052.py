import sys

def compare(a, b):
	for i in range(len(a)):
		if a[i] != b[i]:
			return False
	return True

C = int(sys.stdin.readline())

for c in range(C):
	T = int(sys.stdin.readline())
	numbers = []
	for t in range(T):
		numbers.append(list(sys.stdin.readline().rstrip()))
	numbers.sort()
	# print(numbers)

	flag = True
	for i in range(len(numbers)-1):
		if (compare(numbers[i], numbers[i+1])):
			print('NO')
			flag = False
			break
	if flag:
		print('YES')
		