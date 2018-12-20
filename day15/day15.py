from pprint import *
from queue import PriorityQueue

def manhattanDist(A, B):
	return abs(A[0]-B[0]) + abs(A[1]-B[1])

def readOrderLessThan(A, B):
	return A[1] < B[1] or (A[1] == B[1] and A[0] < B[0])


class Unit(object):
	def __init__(self, location, isGoblin, cave):
		self.isGoblin = isGoblin
		self.loc = location
		self.hp = 200
		self.ap = 3
		self.cave = cave
		self.nextStep = None

	def isAdjacent(self, unit):
		return manhattanDist(self.loc, unit.loc) == 1

	def move(self, openPositions):
		totalPaths = []

		for endPos in openPositions:
			for startPos in self.cave.getOpenAdjacents(self.loc):
				distToP = self.cave.minPath(startPos, endPos)
				if distToP != None:
					totalPaths.append([startPos, endPos, distToP])

		if not totalPaths: 
			return
		if self.loc == (7, 21):
			print(totalPaths)

		minDist = min(totalPaths, key=lambda p: p[2])[2]
		totalPaths = [p for p in totalPaths if p[2] == minDist]

		if len(totalPaths) > 1:
			minTarget = min(totalPaths, key=lambda p: (p[1][1], p[1][0]))[1]
			totalPaths = [p for p in totalPaths if p[1] == minTarget]

		self.nextStep = min(totalPaths, key=lambda p: (p[0][1], p[0][0]))[0]
		if self.loc == (7, 21):
			print(self.nextStep, totalPaths)
		self.cave.moveUnit(self)

	def attack(self, targets):
		targets = [t for t in targets if self.isAdjacent(t)]

		if not targets:
			return
		
		minHP = min(targets, key=lambda t: t.hp).hp
		targets = [t for t in targets if t.hp == minHP]
		targets.sort(key=lambda t: t.loc[1])

		target = targets[0]
		target.hp -= self.ap

		if target.hp <= 0:
			self.cave.delUnitAt(target.loc)

	def turn(self):
		targets = self.cave.targetsFor(self)
		if not targets:
			return -1
		openPositions = []
		for t in targets:
			if self.isAdjacent(t):
				self.attack(targets)
				return 0

			openPositions += self.cave.getOpenAdjacents(t.loc)

		if openPositions:
			self.move(openPositions)

		self.attack(targets)
		return 0

	def __repr__(self):
		ret = 'G' if self.isGoblin else 'E'
		return ret + " " + str(self.loc)

class Cave(object):
	def __init__(self, caveMap):
		self.units = []
		self.caveMap = []
		self.elfCount = 0
		self.gobCount = 0

		for i in range(len(caveMap[0])-1):
			self.caveMap.append([])
			for j in range(len(caveMap)):
				self.caveMap[i].append(caveMap[j][i])

		for i, row in enumerate(caveMap):
			for j, cell in enumerate(row):
				if cell not in 'GE':
					continue

				unit = Unit((j,i), cell == 'G', self)
				if cell == 'G':
					self.gobCount += 1
				else:
					self.elfCount += 1

				self.units.append(unit)

	def readCell(self, loc):
		return self.caveMap[loc[0]][loc[1]]

	def writeCell(self, loc, value):
		self.caveMap[loc[0]][loc[1]] = value

	def moveUnit(self, unit):
		if unit.nextStep:
			self.writeCell(unit.loc, '.')
			self.writeCell(unit.nextStep, 'G' if unit.isGoblin else 'E')
			unit.loc = unit.nextStep

	def delUnitAt(self, loc):
		unit = [u for u in self.units if u != None and u.loc == loc][0]
		self.writeCell(loc, '.')
		self.units[self.units.index(unit)] = None

		if unit.isGoblin:
			self.gobCount -= 1
		else:
			self.elfCount -= 1
		del unit

	def getHPSum(self):
		return sum([u.hp for u in self.units if u != None])

	def getAdjacents(self, loc):
		modifiers = [
			(0,1),
			(1,0),
			(0,-1),
			(-1,0)
		]

		adjacents = []
		for mod in modifiers:
			adjacents.append(tuple(loc[i] + mod[i] for i in [0,1]))
		return adjacents

	def getOpenAdjacents(self, loc):
		return [x for x in self.getAdjacents(loc) if self.readCell(x) == '.']

	def targetsFor(self, unit):
		return [enemy for enemy in self.units if (enemy != None) and enemy.isGoblin ^ unit.isGoblin]

	def minPath(self, locA, locB):
		queue = PriorityQueue()
		queue.put(locA, 0)
		cameFrom = {}
		cost = {}
		cameFrom[locA] = None
		cost[locA] = 0

		if locA == locB:
			return 0

		while not queue.empty():
			current = queue.get()

			if current == locB:
				return cost[current]

			for _next in self.getOpenAdjacents(current):
				newCost = cost[current] + 1

				if _next not in cost or newCost < cost[_next]:
					cost[_next] = newCost

					priority = newCost + manhattanDist(locB, _next)
					queue.put(_next, priority)
					cameFrom[_next] = current

	def run(self, verbose=True):
		if verbose: self.printGraph()
		curRound = 0
		while True:
			self.units.sort(key=lambda unit: unit.loc[1])

			for unit in self.units:
				if unit != None:
					if unit.turn() == -1:
						hpSum = self.getHPSum()
						self.printGraph()
						print(curRound, unit, self.units)
						return curRound, self.getHPSum()

			self.units = [u for u in self.units if u != None]
			curRound += 1
			if verbose: print("Round " + str(curRound))
			if verbose: self.printGraph()			
			#if curRound == 31: exit()

	def printGraph(self):
		for i in range(len(self.caveMap[0])):
			line = ""
			units = []
			for j, col in enumerate(self.caveMap):
				line += col[i]
				if col[i] in 'GE':
					units.append([u for u in self.units if u != None and u.loc == (j,i)][0])
			if units:
				line += "  "
				for u in units:
					line += ' G' if u.isGoblin else ' E'
					line += '(%s),' % str(u.hp)
				line = line[:-1]
			print(line)
		print()

inputs = {
	(47,590):[
		"#######",
		"#.G...#",
		"#...EG#",
		"#.#.#G#",
		"#..G#E#",
		"#.....#",
		"#######",
	],
	(37,982):[	
		"#######",
		"#G..#E#",
		"#E#E.E#",
		"#G.##.#",
		"#...#E#",
		"#...E.#",
		"#######"
	],
	(46,859):[
		"#######",
		"#E..EG#",
		"#.#G.E#",
		"#E.##E#",
		"#G..#.#",
		"#..E#.#",
		"#######"
	],
	(35,793):[
		"#######",
		"#E.G#.#",
		"#.#G..#",
		"#G.#.G#",
		"#G..#.#",
		"#...E.#",
		"#######"
	],
	(54,536):[
		"#######",
		"#.E...#",
		"#.#..G#",
		"#.###.#",
		"#E#G#G#",
		"#...#G#",
		"#######"
	],
	(20,937):[
		"#########",
		"#G......#",
		"#.E.#...#",
		"#..##..G#",
		"#...##..#",
		"#...#...#",
		"#.G...G.#",
		"#.....G.#",
		"#########"
	]
}

caveMap = open("input", 'r').readlines()
cave = Cave(caveMap)
results = print(cave.run())
exit()

for expected, data in inputs.items():
	cave = Cave(data)
	results = cave.run()
	output = "Expected: " + str(expected)
	output += " Got: " + str(results)
	output += " SUCCESS" if results == expected else " FAIL"
	print(output)
