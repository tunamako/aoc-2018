freqDeltas = list(map(int, open("input", "r").readlines()))

# ** Part 1 **
print(sum(freqDeltas))

# ** Part 2 **
freq, i = 0, 0
seenFreqs = set()
while freq not in seenFreqs:
	seenFreqs.add(freq)
	freq += freqDeltas[i%len(freqDeltas)]
	i += 1
print(freq)