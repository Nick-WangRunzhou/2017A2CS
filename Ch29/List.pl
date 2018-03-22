% Last
my_last(X,[X]).

my_last(X,[_|L]) :- 
	my_last(X,L).

% Last but one
last_but_one(X,[X,_]).
last_but_one(X,[_,Y|Ys]) :- 
	last_but_one(X,[Y|Ys]).


