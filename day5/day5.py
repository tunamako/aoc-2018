import cProfile

def react(aString, ignored={}):
	stack = []

	for c in aString:
		if stack and (c ^ stack[-1] == 32):
			del stack[-1]
		elif c not in ignored:
			stack.append(c)
	return stack

def day5():
	_in = map(ord, open("C:\\Users\\Tuna\\Desktop\\input", 'r').readlines()[0])

	#Part 1
	_in = react(_in)
	print(len(_in))
	#Part 2
	lengths = [len(react(_in, {a,a-32})) for a in range(97,123)]
	print(min(lengths))

cProfile.run("day5()")