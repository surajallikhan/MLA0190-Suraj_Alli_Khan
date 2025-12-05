parent(john, bill).
parent(linda, bill).
parent(john, alice).
parent(linda, alice).
parent(bill, bob).
parent(alice, sue).
parent(tom, marry).
parent(susan, marry).
parent(bob, sam).

male(john).
male(bill).
male(bob).
male(tom).
female(linda).
female(sue).
female(marry).
female(susan).

brother(X, Y) :-
	sibling(X, Y),
	male(X).
sister(X, Y) :-
	sibling(X, Y),
	female(X).

father(X, Y) :-
	parent(X, Y),
	male(X).

grandparent(X, Y) :-
	parent(X, Z),
	parent(Z, Y).




grandfather(X, Y) :-
	grandparent(X, Y),
	male(X).
