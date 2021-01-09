import sys
from itertools import permutations

T = int(sys.stdin.readline())
Arr = list(map(int, sys.stdin.readline().split()))
OP = list(map(int, sys.stdin.readline().split()))

def calc(arr, oper):
	res = arr[0]

	for a, o in zip(arr[1:], oper):
		if o == 0: res += a
		elif o == 1: res -= a
		elif o == 2: res *= a
		else: res = int(res/a)
	return res

op = [] 
for i in range(len(OP)):
	for j in range(OP[i]):
		op.append(i)

operators = list(permutations(op))
maxi = -10**9
mini = 10**9

for operator in operators:
	res = calc(Arr, operator)

	if maxi < res: maxi = res
	if mini > res: mini = res

print(maxi)
print(mini)
