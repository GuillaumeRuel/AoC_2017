class AoC_6:

	puzzle = list(map(int, "11 11 13 7 0 15 5 5 4 4 1 1 7 1 15 11".split(' ')))
	print(puzzle)
	#puzzle = "0 2 7 0".split(" ")
	curr_state = ""
	state = []
	n = 0

	while state.count(curr_state) != 2:
		state.append(' '.join(list(map(str, puzzle))))
		m = max(puzzle)
		d = puzzle.index(m)
		puzzle[d] = 0
		d = d + 1

		for i in range(m):
			j = (d + i) % len(puzzle)
			puzzle[j] = puzzle[j] + 1

		curr_state = ' '.join(list(map(str, puzzle)))

		if curr_state in state:
			n += 1

	print('n ', n - 1)

if __name__ == "__main__":
	AoC_6()