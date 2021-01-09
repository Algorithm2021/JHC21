import sys

T = int(sys.stdin.readline())
Arr = list(map(int, sys.stdin.readline().split()))
check = [False for i in range(len(Arr))]

def get_energy(arr, checked):
	res = 0

	for i in range(1, len(Arr)-1):
		if (checked[i]): continue
		left = i-1
		right = i+1

		while(checked[left]): left-=1
		while(checked[right]): right+=1
		checked[i] = True

		res = max(res, get_energy(arr, checked) + arr[left] * arr[right])
		checked[i] = False

	return res

print(get_energy(Arr,check))