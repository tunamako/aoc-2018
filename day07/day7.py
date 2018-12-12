import cProfile
from pprint import *

def genRelationDict(relations):
	relationDict = dict((chr(a),set()) for a in range(65,91))
	for r in relations:
		relationDict[r[36]].add(r[5])
	return relationDict

def day7(relations, workerCount):
	relationDict = genRelationDict(relations)
	available, doneSteps = [], []
	workers = [[]]*workerCount
	time = 0

	while relationDict or sum(map(bool, workers)):
		for step, preReqs in relationDict.items():
			relationDict[step] -= set(doneSteps)

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
				doneSteps.append(w[0])
				workers[i] = []

	return time, ''.join(doneSteps)

relations = open("input", 'r').readlines()
print(day7(relations, 1))
print(day7(relations, 5))
