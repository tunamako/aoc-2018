def power(x,y):
	p = str((x+10) * ((x + 10) * y + serial))
	if len(p) < 3:
		return -5

	return int(p[-3]) - 5

def getSquareDimPower(dim):
	maxPower = [(0,0),0]
	for x in range(1,301-dim+1):
		for y in range(1,301-dim+1):
			p = 0
			for i in range(dim):
				p += sum(grid[x+i][y:y+dim])

			if p > maxPower[1]:
				maxPower = [(x,y),p]
	return maxPower

serial = 5093
grid = [[0 for x in range(301)] for y in range(301)]

for x in range(1,301):
	for y in range(1,301):
		grid[x][y] = power(x,y)

# Part 1
maxPower = [(0,0),0]
for x in range(1,299):
	for y in range(1,299):
		p = sum(grid[x][y:y+3]) + sum(grid[x+1][y:y+3]) + sum(grid[x+2][y:y+3])

		if p > maxPower[1]:
			maxPower = [(x,y),p]
print(maxPower)

# Part 2
maxTotal = [(0,0),0,0]
for i in range(1,301):
	p = getSquareDimPower(i)
	if p[1] > maxTotal[2]:
		maxTotal = [p[0], i, p[1]]
		print(maxTotal)
