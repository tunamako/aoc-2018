from collections import Counter
from pprint import *
import cProfile
points = {tuple(map(int, p.split(', '))) for p in open("input", 'r').readlines()}
maxX = max(points, key=lambda x: x[0])[0]
maxY = max(points, key=lambda x: x[1])[1]
 
grid = [[0 for y in range(maxY)] for x in range(maxX)]

def manDist(a,b):
	return abs(b[0]-a[0]) + abs(b[1]-a[1])

def part1(points):
	for x in range(maxX):
		for y in range(maxY):
			if (x,y) in points: continue

			mindist = min(manDist((x,y),p) for p in points)

			for p in points:
				if manDist((x,y), p) == mindist:
					if grid[x][y] in points:
						grid[x][y] = 0
						break
					grid[x][y] = p

	toBeDeleted = set()
	points = Counter(points)

	for x in range(maxX):
		for y in range(maxY):
			if x in [0,maxX-1] or y in [0,maxY-1]:
				toBeDeleted.add(grid[x][y])
			else:
				points[grid[x][y]] += 1

	for p in toBeDeleted:
		del points[p]
	del points[0]

	return points.most_common()[0][1]

def part2(points):
	total = 0
	for x in range(-200, maxX + 200):
		for y in range(-200, maxY + 200):
			if sum([manDist((x,y), p) for p in points]) < 10000:
				total +=1
	return total

def day6():
	print(part1(points))
	print(part2(points))

cProfile.run("day6()")
