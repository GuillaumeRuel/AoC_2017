
groups = []
comm_dict = {}

with open('data/AoC_12.txt', newline='') as f:
	puzzle = [line for line in f]

	visited_prog = []
	first_prog = '0'
	search = ['0']
	has_found_prog = True
	while len(search) != 0:
		while len(search) != 0:
			for line in puzzle:
				line = line.replace('\r', '').replace('\n', '').split(' <-> ')
				l_prog = line[0]
				r_prog = line[1].split(', ')
				if l_prog in search:
					comm_dict[l_prog] = r_prog
					search.remove(l_prog)
					visited_prog.append(l_prog)
					for prog in r_prog:
						if not prog in visited_prog:
							search.append(prog)
		groups.append(first_prog)

		for line in puzzle:
			line = line.replace('\r', '').replace('\n', '').split(' <-> ')
			l_prog = line[0]
			if not l_prog in comm_dict.keys():
				search.append(l_prog)
				first_prog = l_prog
				break

print(len(groups))





