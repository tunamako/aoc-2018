def expandPots(pots, rules, zeroIndex):
	for i in range(1,5):
		if rules['.' * i + pots[:5-i]] == '#':
			pots = '.' * i + pots
			zeroIndex += i
		if rules[pots[-5+i:] + '.' * i] == '#':
			pots += '.' * i
	return pots, zeroIndex

def applyRules(pots, rules):
	temp = list(pots)
	usedRules = set()
	for i in range(2, len(pots)-2):
		chunk = pots[i-2:i+3]
		temp[i] = rules[chunk]
		usedRules.add(chunk)

	return ''.join(temp), usedRules

data = open("input", 'r').readlines()
pots = data[0][15:-1]
rules = dict(rule[:-1].split(' => ') for rule in data[2:])

zeroIndex = 0
gen = 0
lastUsedRules = set()

while True:
	if gen == 20:
		partOneState = pots

	pots, zeroIndex = expandPots(pots, rules, zeroIndex)
	pots, usedRules = applyRules(pots, rules)

	if usedRules == lastUsedRules:
		break

	lastUsedRules = usedRules
	gen += 1

print(sum([i-zeroIndex for i in range(len(partOneState)) if partOneState[i] == '#']))
print(sum([i-zeroIndex+(50000000000-gen) for i in range(len(pots)) if pots[i] == '#']))
