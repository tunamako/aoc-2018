nextLocations = {
	'>': (+1, 0),
	'<': (-1, 0),
	'^': (0, -1),
	'v': (0, +1),
}
nextFacings = {
	'>\\': 'v',
	'>/': '^',
	'<\\': '^',
	'</': 'v',
	'^/': '>',
	'^\\': '<',
	'v/': '<',
	'v\\': '>',
}
turnStates = {
	'>': ['^','>','v'],
	'<': ['v','<','^'],
	'^': ['<','^','>'],
	'v': ['>','v','<'],
}

class Cart(object):
	def __init__(self, location, grid):
		self.facing = grid.read(location)
		self.location = location
		self.turnCount = 0		
		self.sittingOn = '-' if self.facing in '<>' else '|'

	def __str__(self):
		return self.facing + ',' + str(self.location)

	def __repr__(self):
		return str(self)

	def setFacing(self, nextTile):
		if nextTile in '/\\':
			self.facing = nextFacings[self.facing+nextTile]
		elif nextTile == '+':
			self.facing = turnStates[self.facing][self.turnCount % 3]
			self.turnCount += 1

	def step(self, grid):
		nextLoc = tuple(self.location[i] + nextLocations[self.facing][i] for i in (0,1))
		nextTile = grid.read(nextLoc)

		if nextTile in '^v<>':
			return nextLoc

		self.setFacing(nextTile)

		grid.write(self.location, self.sittingOn)
		grid.write(nextLoc, self.facing)
		self.sittingOn = nextTile
		self.location = nextLoc

class Grid(object):
	def __init__(self, rails):
		self.grid = []
		self.carts = []

		for x in range(len(rails[0])-1):
			self.grid.append([])
			for y in range(len(rails)):
				self.grid[x].append(rails[y][x])
				if self.grid[x][y] in "v^<>":
					self.carts.append(Cart((x,y), self))

	def read(self, loc):
		return self.grid[loc[0]][loc[1]]

	def write(self, loc, value):
		self.grid[loc[0]][loc[1]] = value

	def run(self, stopAtCollision=True):
		while len(self.carts) > 1:
			self.carts.sort(key=lambda c: c.location)

			temp = self.carts[:]
			for cart in temp:
				if cart not in self.carts:
					continue
				collisionLoc = cart.step(self)

				if not collisionLoc:
					continue
				if stopAtCollision:
					return collisionLoc

				otherCart = [c for c in temp if c.location == collisionLoc][0]
				self.write(cart.location, cart.sittingOn)
				self.write(otherCart.location, otherCart.sittingOn)
				del self.carts[self.carts.index(cart)]
				del self.carts[self.carts.index(otherCart)]

		return self.carts[0].location

rails = open("input", 'r').readlines()
print(Grid(rails).run())
print(Grid(rails).run(stopAtCollision=False))
