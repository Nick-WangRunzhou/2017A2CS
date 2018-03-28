/*Factorial*/ 
factorial(0,1).
factorial(N,F) :-
     X is N-1,
     factorial(X,Y),
     F is N*Y. 

/*BunnyEars*/
bunnyEars(0, 0).
bunnyEars(A, B) :-
	X is A - 1,
	bunnyEars(X, Y),
	B is Y + 2.

/*Fib*/
fib(0,0)
fib(1,1)
fib(N,F):-
	A is N -1,
	B is N -2,
	fib(A,C),
	fib(B,D),
	F is C+D.

/* Bunny ears 2 */
bunnyEars2(0, 0).
bunnyEars2(1, 2).
bunnyEars2(2, 5).
bunnyEars2(Input, Output) :-
	Pre is Input - 2,
	bunnyEars2(Pre, PreResult),
	Output is PreResult + 5.

/* triangle */
triangle(0, 0).
triangle(1, 1).
triangle(Row, Sum) :-
	PreRow is Row - 1,
	triangle(PreRow, PreSum),
	Sum is PreSum + Row..
 

/* sum digit */
sumDigits(0, 0).
sumDigits(N, S) :-
	PreN is div(N,10),
	sumDigits(PreN, PreS),
	S is PreS + mod(N,10).

/* count 7 */
isSeven(7).
countSeven(0, 0).
countSeven(N,C) :-
	D is mod(N,10),
	PreN is div(N,10),
	countSeven(PreN,PreS),
	( ( isSeven(D), C is PreS + 1 );
	( not(isSeven(D)), C is PreS + 0 ) ).


     
     


