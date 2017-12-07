class AoC_7:

	puzzle = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)""".split('\n')

	leftline = []
	rightrow = []

	with open('data/AoC_7.txt', newline='') as f:

		for line in f:
			if "->" in line:

				line = line.replace('\r', '').replace('\n', '')
				entry = line.split(' -> ')
				leftline.append(entry[0].split(' (')[0])
				rightrow += entry[1].split(', ')

	for l in leftline:
		if l not in rightrow:
			print(l)

if __name__ == "__main__":
	AoC_7()