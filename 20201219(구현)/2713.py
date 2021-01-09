n = int(input())
for a in range(n):
	line = input()
	h, w = int(line.split()[0]), int(line.split()[1]) 
	words, code = [], ''

	for word in line[2 + (2 if w//10 > 0 else 1) +(2 if h//10 > 0 else 1):]:
		if (word == ' '): words+=[0]
		else: words += [ord(word)-64]
	print(words)
	for l in words: code += '0' * (5 - len(bin(l)) + 2) + bin(l)[2:]
	if (len(code) < w*h): code = code + '0'*(w*h - len(code))
	matrix = [[None] * w for _ in range(h)]

	idx, start_x, end_x, start_y, end_y = 0, 0, (w), 0, (h)

	while (start_x < end_x and start_y < end_y):
		for i in range(start_x, end_x):
			matrix[start_y][i] = code[idx]
			idx+=1
		start_y += 1

		for i in range(start_y, end_y):
			matrix[i][end_x-1] = code[idx]
			idx+=1
		end_x-=1

		if (start_y < end_y):
			for i in range(end_x-1, start_x-1, -1):
				matrix[end_y-1][i] = code[idx]
				idx+=1
			end_y-=1

		if (start_x < end_x):
			for i in range(end_y-1, start_y-1, -1):
				matrix[i][start_x] = code[idx]
				idx+=1
			start_x+=1

	print(''.join(''.join(mat) for mat in matrix))
