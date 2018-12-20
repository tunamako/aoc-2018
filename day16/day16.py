from pprint import *
from collections import defaultdict

opcodes = {
	"addr": lambda A, B, reg: reg[A] + reg[B],
	"addi": lambda A, B, reg: reg[A] + B,
	"mulr": lambda A, B, reg: reg[A] * reg[B],
	"muli": lambda A, B, reg: reg[A] * B,
	"banr": lambda A, B, reg: reg[A] & reg[B],
	"bani": lambda A, B, reg: reg[A] & B,
	"borr": lambda A, B, reg: reg[A] | reg[B],
	"bori": lambda A, B, reg: reg[A] | B,
	"setr": lambda A, B, reg: reg[A],
	"seti": lambda A, B, reg: A,
	"gtir": lambda A, B, reg: int(A > reg[B]),
	"gtri": lambda A, B, reg: int(reg[A] > B),
	"gtrr": lambda A, B, reg: int(reg[A] > reg[B]),
	"eqir": lambda A, B, reg: int(A == reg[B]),
	"eqri": lambda A, B, reg: int(reg[A] == B),
	"eqrr": lambda A, B, reg: int(reg[A] == reg[B]),
}

possibleOps = defaultdict(set)

def getValidOps(before, instruction, after):
	A, B, C = instruction[1:]
	count = 0
	for op in opcodes:
		if opcodes[op](A, B, before) == after[C]:
			possibleOps[op].add(instruction[0])
			count += 1
	return count

_input = open("input", 'r').readlines()

i = 0
count = 0
while _input[i][0] == 'B':
	before, instruction, after = [line[:-1] for line in _input[i:i+3]]
	
	before 		= [int(j) for j in before[9:-1].split(', ')]
	instruction = [int(j) for j in instruction.split(' ')]
	after 		= [int(j) for j in after[9:-1].split(', ')]

	if getValidOps(before, instruction, after) >= 3:
		count += 1

	i+= 4

while True:
	singleOpCode = None
	for op, codes in possibleOps.items():
		if codes != None and len(codes) == 1:
			singleOpCode = codes.pop()
			possibleOps.pop(op)
			opcodes[singleOpCode] = opcodes.pop(op)
			break

	if singleOpCode == None:
		break

	for op, codes in possibleOps.items():
		try:
			possibleOps[op].remove(singleOpCode)
		except:
			pass

registers = [0,0,0,0]

i += 2
while _input[i][0] != '\n':
	op, A, B, C = [int(j) for j in _input[i].split(' ')]
	registers[C] = opcodes[op](A,B,registers)
	i += 1
print(count)
print(registers[0])
