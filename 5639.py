stack = [int(input())]

while(1):
	try: 
		num = int(input())
		if (stack[-1] > num):
			stack.append(num)
		else:
			print(num, stack)
			if (len(stack) > 2):
				if (stack[-2] > stack[-1]):
					while (stack[-2] < num):
						print(stack.pop())
						if (len(stack)<2): break
				else:
					while (stack[-2] > num):
						print(stack.pop())
						if (len(stack)<2): break
				stack.append(num)
	except: break

for st in stack[::-1]:
	print(st)
