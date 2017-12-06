class AoC_4:

	n = 0
	with open('data/AoC_4.txt', newline='') as f:

		for line in f:
			s = [''.join(sorted(x)) for x in line.split()]
			if len(line.split()) == len(list(set(line.split()))) and len(s) == len(list(set(s))):
				n += 1

		print(n)


if __name__ == "__main__":
	AoC_4()