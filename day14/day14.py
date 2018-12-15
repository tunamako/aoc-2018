import cProfile

def part1():
	_in = 165061
	recipes = [3,7]
	A = 0
	B = 1

	while len(recipes) < _in + 10:
		recipes += map(int, str(recipes[A]+recipes[B]))
		A = (A + recipes[A] + 1) % len(recipes)
		B = (B + recipes[B] + 1) % len(recipes)

	return ''.join(map(str, recipes[_in:_in+10]))

def part2():
	target = "165061"
	tarLen = len(target)
	recipes = "37"
	A = 0
	B = 1
	startIndex = 0
	recipeCount = 2

	while target not in recipes[startIndex:]:
		addition = str(int(recipes[A])+int(recipes[B]))
		addLen = len(addition)
		recipes += addition
		recipeCount += addLen
		A = (A + int(recipes[A]) + 1) % recipeCount
		B = (B + int(recipes[B]) + 1) % recipeCount

		if recipeCount-addLen > tarLen:
			startIndex += addLen

	return recipes.index(target)

print(part1())
print(part2())