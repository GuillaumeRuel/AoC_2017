from anytree import Node, RenderTree
import re


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
	
data_tree = []
prog_weight = {}
nodes = {}
base = ""

def total_weight_node(name):
	if nodes[name].is_leaf:
		return nodes[name].weight
	else:
		d = [str(x).split("',")[0].split('/')[-1] for x in nodes[name].children]
		return nodes[name].weight + sum([total_weight_node(x) for x in d])

with open('data/AoC_7.txt', newline='') as f:

	puzzle = [line for line in f]

	for line in puzzle:
		line = line.replace('\r', '').replace('\n', '')
		entry = line.split(' -> ')
		node = entry[0].split(' (')[0].strip()
		node_weight = re.findall(r'\d+', entry[0])[0]

		prog_weight[node] = node_weight

	for line in puzzle:

		if '->' in line:
			line = line.replace('\r', '').replace('\n', '')
			entry = line.split(' -> ')
			node = entry[0].split(' (')[0].strip()
			child = entry[1].split(', ')

			if node == 'dgoocsw':
				a = Node('dgoocsw', weight=int(prog_weight[node]))
				nodes[node] = a

			try:
				n = nodes[node]
				for c in child:
					a = Node(c, parent=n, weight=int(prog_weight[c]))
					nodes[c] = a
			except KeyError:
				puzzle.append(line)


for key, value in nodes.items():
	nodes[key].weight = total_weight_node(key)

for pre, fill, node in RenderTree(nodes['dgoocsw']):
	print("%s%s" % (pre, node))


