import sys

# line = sys.stdin.readline()
line = '0'

origin, next_v, count = int(line), int(line), 0

while(True):
	next_v = ((next_v//10 + next_v%10)%10)+(next_v%10)*10
	count+=1
	if not (origin != next_v): break

print(count)
