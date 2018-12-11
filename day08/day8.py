import cProfile
data = list(map(int, open("bigboy", 'r').readlines()[0].split(' ')))

def part1(i=0):
	metaDataSum, nodeLen = 0, 2

	for child in range(data[i]):
		childLen, childData = part1(i + nodeLen)
		metaDataSum += childData
		nodeLen += childLen

	metaDataSum += sum(data[i + nodeLen:i + nodeLen+data[i+1]])

	return nodeLen + data[i+1], metaDataSum

def part2(i=0):
	metaDataSum = 0
	nodeLen = 2
	children = [None]

	for child in range(data[i]):
		childLen, childData = part2(i + nodeLen)
		children.append(childData)
		nodeLen += childLen

	metaData = data[i+nodeLen:i+nodeLen+data[i+1]]
	
	for m in metaData:
		if data[i] and m < len(children):
			metaDataSum += children[m]
		elif data[i] == 0:
			metaDataSum += m

	return nodeLen + data[i+1], metaDataSum

def day8():
	print(part1())
	print(part2())
cProfile.run('day8()')