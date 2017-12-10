from functools import reduce

puzzle = list(map(ord, "102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216")) + [17, 31, 73, 47, 23]
#puzzle = list(map(ord, "AoC 2017")) + [17, 31, 73, 47, 23]
c_list = [x for x in range(256)]

n = 0
curr_pos = 0

for r in range(64):
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

dense_hash = [reduce(lambda i, j: i ^ j, c_list[x*16:(x+1)*16]) for x in range(16)]
knot_hash = ''.join(['{0:02x}'.format(x) for x in dense_hash])

print(knot_hash)
