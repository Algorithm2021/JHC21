import sys
from collections import deque

prev_line = deque(list(sys.stdin.readline().rstrip()))
next_line = deque()
t=int(sys.stdin.readline())
print(prev_line)
print(next_line)
for i in range(t):
    cmd =sys.stdin.readline()

    if cmd[0] == 'L': 
        if prev_line:
        	next_line.appendleft(prev_line.pop())
    elif cmd[0] == 'D': 
        if next_line:
        	prev_line.append(next_line.popleft())
    elif cmd[0] == 'B':
    	if prev_line:
            prev_line.pop()
    elif cmd[0] == 'P':
        prev_line.append(cmd[2])
        
print(''.join(list(prev_line)), end='')
print(''.join(list(next_line)))