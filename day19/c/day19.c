#include <stdio.h>
#include <stdlib.h>

int reg[6] = {1,0,0,0,0,0};

int addr(int A, int B) {
	return reg[A] + reg[B];
}
int addi(int A, int B) {
	return reg[A] + B;
}
int mulr(int A, int B) {
	return reg[A] * reg[B];
}
int muli(int A, int B) {
	return reg[A] * B;
}
int setr(int A, int B) {
	return reg[A];
}
int seti(int A, int B) {
	return A;
}
int gtrr(int A, int B) {
	return (int)(reg[A] > reg[B]);
}
int eqrr(int A, int B) {
	return (int)(reg[A] == reg[B]);
}

int (*ptf[8])(int A, int B) = {addr,addi,mulr,muli,setr,seti,gtrr,eqrr};

void main() {
	int **pgm = (int**)malloc(36*sizeof(int*));
	for(int i = 0; i < 36; i++) {
		pgm[i] = malloc(4*sizeof(int));
	}

	FILE *input = fopen("A:\\Documents\\aoc-2018\\day19\\c\\input", "r");
	if (input == NULL) {
		exit(EXIT_FAILURE);
	}

	for (int i = 0; i < 36; i++) {
		for (int j = 0; j < 4; j++) {
			if (!fscanf(input, "%ld", &pgm[i][j]))
				break;
		}
	}
	fclose(input);

	int ipReg = 5;
	int ip = 0;

	while(ip < 36) {
		reg[ipReg] = ip;
		int *inst = pgm[ip];
		reg[inst[3]] = (*ptf[inst[0]])(inst[1], inst[2]);

		ip = reg[ipReg] + 1;
	}

	for(int i = 0; i<6; i++) {
		printf("%d ", reg[i]);
	}
	printf("\n");

	for (int i = 0; i < 36; i++) {
		free(pgm[i]);
	}
	free(pgm);
}