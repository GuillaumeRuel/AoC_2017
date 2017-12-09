puzzle = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10""".split('\n')

data_dict = {}
max_val = 0

with open('data/AoC_8.txt', newline='') as f:

	for line in f:

		d = line.split(' ')
		var1 = 0
		var2 = 0

		try:
			var1 = int(data_dict[d[0]])
		except KeyError:
			data_dict[d[0]] = 0

		try:
			var2 = int(data_dict[d[-3]])
		except KeyError:
			data_dict[d[-3]] = 0

		s = ' '.join([str(var2), d[-2], d[-1]])
		if eval(s):
			if d[1] == 'inc':
				data_dict[d[0]] = var1 + int(d[2])
			elif d[1] == 'dec':
				data_dict[d[0]] = var1 - int(d[2])

		if data_dict[d[0]] > max_val:
			max_val = data_dict[d[0]]


data = []
for key, value in data_dict.items():
	data.append(int(value))

print("Max ", max(data))
print("Max value ever! ", max_val)










