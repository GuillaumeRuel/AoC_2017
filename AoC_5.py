class AoC_5:

	step = 0
	maze = []
	i = 0
	pos = 0

	with open('data/AoC_5.txt', newline='') as f:
		for line in f:
			maze.append(int(line))

	print('len', len(maze))

	while pos < len(maze) and pos >= 0:
		offset = maze[pos]
		maze[pos] = maze[pos] + 1 if maze[pos] < 3 else maze[pos] - 1
		pos += offset
		step+=1

	print('--------------')
	print('steps : ', step)

if __name__ == "__main__":
	AoC_5()