import cProfile
_input = open("input", 'r').readlines()

def day19():
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

	ipReg = int(_input[0][4])
	instructions = [line[:-1].split(' ') for line in _input[1:]]

	registers = [0,0,0,0,0,0]
	ip = 0
	while ip < len(instructions):
		registers[ipReg] = ip
		inst = instructions[ip]
		op = inst[0]
		A = int(inst[1])
		B = int(inst[2])
		C = int(inst[3])
		registers[C] = opcodes[op](A,B,registers)

		ip = registers[ipReg] + 1

	print(registers)

cProfile.run("day19()")