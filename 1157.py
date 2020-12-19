import sys
from collections import Counter

line = sys.stdin.readline()
count = Counter(line.upper())
max_v = max(count.values())
answer = list(filter(lambda x:x[1] == max_v, count.items()))
print('?' if len(answer)>1 else answer[0][0])
