import gc
import cProfile
import collections

def day9(playerCount, maxMarble):
	players = [0] * playerCount
	circle = collections.deque([0])

	for i in range(1, maxMarble+1):
		if i % 23:
			circle.rotate(-1)
			circle.append(i)
		else:
			circle.rotate(7)
			players[i % playerCount] += i + circle.pop()
			circle.rotate(-1)

	return max(players)

data = open("input", 'r').read().split(' ')
playerCount, maxMarble = int(data[0]), int(data[6])
gc.disable()

print(day9(playerCount, maxMarble))
print(day9(playerCount, maxMarble * 100))
