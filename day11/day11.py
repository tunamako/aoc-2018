def power(x,y):
	p = str((x+10) * ((x + 10) * y + serial))
	if len(p) < 3:
		return -5

	return int(p[-3]) - 5

def getSquareDimPower(dim):
	maxPower = [(0,0),0]
	for x in range(1,301-dim+1):
		for y in range(1,301-dim+1):
			p = grid[x][y][1]

			if dim != 1:
				p += sum([grid[x+dim-1][y+j][0] for j in range(dim)])
				p += sum([grid[x+i][y+dim-1][0] for i in range(dim)])
				p -= grid[x+dim-1][y+dim-1][0]
				grid[x][y][1] = p

			if p > maxPower[1]:
				maxPower = [(x,y),p]
	return maxPower



serial = 5093
grid = [[0 for x in range(301)] for y in range(301)]

"""
		#power, biggestDim, biggestDim's power
point = [0, 0]
"""

for x in range(1,301):
	for y in range(1,301):
		grid[x][y] = [power(x,y)]
		grid[x][y].append(grid[x][y][0])
# Part 1
print(getSquareDimPower(1))
print(getSquareDimPower(2))
print(getSquareDimPower(3))
# Part 2
maxTotal = [(0,0),0,0]
for i in range(4,301):
	p = getSquareDimPower(i)
	print(i)
	if p[1] > maxTotal[2]:
		maxTotal = [p[0], i, p[1]]
		print(maxTotal)

print(maxTotal)
