puzzle = list(map(int, "102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216".split(',')))
c_list = [x for x in range(256)]

n = 0
curr_pos = 0

#puzzle = [3, 4, 1, 5, 0]
#c_list = [x for x in range(5)]

for p in puzzle:

	if p != 0:
		a = curr_pos % len(c_list)
		b = (a + p) % len(c_list)
		sub_list = c_list[a:b] if a < b else c_list[a:] + c_list[:b]
		if a < b:
			c_list[a:b] = sub_list[::-1]
		else:
			s = sub_list[::-1]
			c_list[a:] = s[:len(c_list) - a]
			c_list[:b] = s[len(c_list) - a:]

	curr_pos += p + n
	n += 1

print(c_list[0] * c_list[1])
