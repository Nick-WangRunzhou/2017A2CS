A -  2 LDM #2
	STO A
B - 10 LDM #10
	STO B
C - A + B LDD A
	ADD B
	STO C
D - A - B LDD B 
	XOR #&FF 
	INC ACC 
	ADD A 
	STO D