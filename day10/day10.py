import cProfile

precision = 200

def printGrid(points):
	points = [tuple(p[0]) for p in points]
	minY = min(points, key=lambda p: p[1])[1]
	maxY = max(points, key=lambda p: p[1])[1]
	minX = min(points, key=lambda p: p[0])[0]
	maxX = max(points, key=lambda p: p[0])[0]

	for x in range(minY, maxY+1):
		string = ""
		for y in range(minX, maxX+1):
			if (y,x) in points:
				string += '#'
			else:
				string += '.'
		print(string)

def day9():
	data = open("input", 'r').readlines()
	points = []
	for line in data:
		pos = list(map(int, line[10:line.find('>')].split(', ')))
		v = tuple(map(int, line[line.find('<',11)+1:-2].split(', ')))
		points.append((pos,v))

	sec = 0
	while max(points, key=lambda p: p[0][1])[0][1] - min(points, key=lambda p: p[0][1])[0][1] >= 10:
		for i, p in enumerate(points):
			p[0][0] += p[1][0]
			p[0][1] += p[1][1]

		sec += 1

	printGrid(points)
	print(sec)

day9()
#cProfile.run("print(day9(playerCount, maxMarble * 100))")
