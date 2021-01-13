import sys

line1 = sys.stdin.readline().rstrip()
line2 = sys.stdin.readline().rstrip()

count = [[0 for i in range(len(line1)+1)] for j in range(len(line2)+1)]

for i in range(len(line2)):
	for j in range(len(line1)):
		if line1[j] == line2[i]:
			count[i+1][j+1] = count[i][j] + 1		
		else:
			count[i+1][j+1] = max(count[i+1][j], count[i][j+1])

print(count[-1][-1])