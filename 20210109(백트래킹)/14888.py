import sys
from itertools import permutations

T = int(sys.stdin.readline())
Arr = list(map(int, sys.stdin.readline().split()))
OP = list(map(int, sys.stdin.readline().split()))

def calc(arr, oper):
	res = arr[0]

	for i in range(len(oper)):
		if oper[i] == 0: res += arr[i+1]
		elif oper[i] == 1: res -= arr[i+1]
		elif oper[i] == 2: res *= arr[i+1]
		else: res = int(res/arr[i+1])
		
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
