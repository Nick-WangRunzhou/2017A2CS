parents(harry,jack).
parents(erin,jack).
parents(harry,ann).
parents(erin,ann).
parents(nick,harry).

male(jack).
male(harry).
male(nick).
female(ann).
female(erin).

vegetable(tomato).
vegetable(potato).
meat(chicken).
meat(lamb).
meat(beef).

ingredient(tomato,chsoup,100).
ingredient(chicken,chsoup,250).
ingredient(potato,chsoup,50).
ingredient(souce,chsoup,20).



brother(X,Y) :-
	parents(_,X),
	parents(_,Y),
	male(X).
	
sister(X,Y):-
	parents(_,X),
	parents(_,Y),
	female(X).
son(X,Y):-
	parents(Y,X),
	male(X).
daughter(X,Y):-
	parents(Y,X),
	female(X).
married(X,Y):-
	parents(X,_),
	parents(Y,_),
	male(X) ,female(Y).
married(X,Y):-
	parents(X,_),
	parents(Y,_),
	male(Y),female(X).
ancestor(X,Y):-
	parents(_,Y),parents(X,_).




