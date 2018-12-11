from collections import Counter

boxIDs = open("input", 'r').readlines()

# ** Part 1 **
twos, threes = 0,0

for boxID in boxIDs:
	boxID = Counter(boxID).values()
	if 2 in boxID: twos += 1
	if 3 in boxID: threes += 1

print(twos * threes)


# ** Part 2 **
def stringDiff(A, B):
	diffIndices = []
	for i, (a, b) in enumerate(zip(A, B)):
		if a != b:
			diffIndices.append(i)
	return diffIndices

for x in boxIDs:
	for y in boxIDs:
		diffIndices = stringDiff(x, y) 
		if len(diffIndices) == 1:
			x = list(x)[:-1]
			del x[diffIndices[0]]
			print(''.join(x))
			exit()