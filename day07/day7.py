import cProfile
from pprint import *

relations = open("input", 'r').readlines()

def genRelationDict():
	relationDict = dict((chr(a),set()) for a in range(65,91))
	for r in relations:
		relationDict[r[36]].add(r[5])
	return relationDict

# Part1
relationDict = genRelationDict()
available, doneSteps = [], []

while relationDict:
	for step, preReqs in relationDict.items():
		relationDict[step] -= set(doneSteps)

		if relationDict[step] or step in available:
			continue
		available.append(step)
		del relationDict[step]

	available.sort(reverse=True)
	doneSteps.append(available.pop())

print(''.join(doneSteps))

# Part 2
relationDict = genRelationDict()
available, doneSteps = [], set()
workers = [[]]*5
time = 0

while relationDict or sum(map(bool, w)):
	for step, preReqs in relationDict.items():
		relationDict[step] -= doneSteps

		if relationDict[step] or step in available:
			continue
		available.append(step)
		del relationDict[step]

	available.sort(reverse=True)

	for i, w in enumerate(workers):
		if w or not available:
			continue
		step = available.pop()
		workers[i] = [step, ord(step) - 4]

	chunk = min(workers, key=lambda x: float('inf') if not x else x[1])[1]
	time += chunk

	for i, w in enumerate(workers):
		if not w: continue
		workers[i] = [w[0], w[1]-chunk]

		if workers[i][1] == 0:
			doneSteps.add(w[0])
			workers[i] = []

print(time)