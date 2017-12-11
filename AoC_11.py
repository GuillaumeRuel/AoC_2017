direction = [0, 0]
point = {'n':[0, 1], 'nw':[-1, 0], 'sw':[-1, -1], 's':[0, -1], 'se':[1, 0], 'ne':[1, 1] }
max_step = 0

def count_step(coord):
	if coord[0] < 0 and coord[1] < 0 or coord[0] > 0 and coord[1] > 0:
		return abs(coord[0])
	elif coord[0] < 0 and coord[1] > 0 or coord[0] > 0 and coord[1] < 0:
		return abs(coord[0]) + abs(coord[1])
	else:
		return 0

def adjust_path(coord):
	direction[0] = direction[0] + coord[0]
	direction[1] = direction[1] + coord[1]

	global max_step
	steps = count_step(direction)
	if steps > max_step:
		max_step = steps

with open('data/AoC_11.txt', newline='') as f:
	path = next(f).split(',')

	for step in path:
		adjust_path(point.get(step))

print('Final coord :', direction)
print('Steps :', count_step(direction))
print('Max steps :', max_step)
