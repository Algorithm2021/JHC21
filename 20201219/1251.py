import sys

#line = sys.stdin.readline()
line = 'zzzzzab'
ans = []

for i in range(len(line)-2):
	for j in range(i+1,len(line)-1):
		ans.append(line[i::-1] + line[j:i:-1] + line[:j:-1])
ans.sort()
print(ans[0])


