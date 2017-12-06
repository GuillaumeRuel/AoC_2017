class AoC_3:

	def spiral(N, M):
	    x,y = 0,0   
	    dx, dy = 0, -1
	    n = 1
	    grid = [tuple([1,0,0])]
	    grid_list = [[1,0,0]]

	    for z in range(N*M):
	        if abs(x) == abs(y) and [dx,dy] != [1,0] or x>0 and y == 1-x:  
	            dx, dy = -dy, dx

	        if abs(x)>N/2 or abs(y)>M/2:
	            dx, dy = -dy, dx
	            x, y = -y+dx, x+dy       

	        x, y = x+dx, y+dy

	        gt = set(tuple([x[1:] for x in grid]))

	        l = [[x+1, y], [x+1, y+1], [x , y+1], [x-1, y+1], [x-1, y], [x-1, y-1], [x, y-1], [x+1, y-1]]
	        sg = set(tuple(i) for i in l)

	        inter = sg & gt
	        data = map(list, inter)
	        n = 0

	        for d in data:
	        	for p in grid_list:
	        		if d == p[1:]:
	        			n += p[0]
	        

	        grid.append(tuple([n,x,y]))
	        grid_list.append([n,x,y])

	    return grid_list

	g = spiral(10,10)
	print(g)

	for x in g:
		if x[0] >= 361527:
			print(x)
			break

if __name__ == "__main__":
	AoC_3()