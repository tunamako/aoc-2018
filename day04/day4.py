import cProfile
from collections import defaultdict


def day4():
	records = open("bigboy", 'r').readlines()
	records.sort()
	guards = defaultdict(lambda: [0] * 60)

	for event in records:
		if "Guard" in event:
			curGuard = event[26:event.find(' ', 26)]
		elif "falls" in event:
			sleepStart = int(event[15:17])
		else:
			for i in range(sleepStart, int(event[15:17])):
				guards[curGuard][i] += 1

	# id, minute, value
	laziestGuard = [0, 0, 0]
	sleepiestMinute = [0, 0, 0]

	for guard, minutes in guards.items():
		curLaziness = sum(minutes)
		curMaxMinuteValue = max(minutes)
		curMaxMinute = minutes.index(curMaxMinuteValue)

		if curLaziness > laziestGuard[2]:
			laziestGuard = guard, curMaxMinute, curLaziness		
		if curMaxMinuteValue > sleepiestMinute[2]:
			sleepiestMinute = guard, curMaxMinute, curMaxMinuteValue

	# Part 1
	print(int(laziestGuard[0]) * laziestGuard[1])
	# Part 2
	print(int(sleepiestMinute[0]) * sleepiestMinute[1])

cProfile.run('day4()')