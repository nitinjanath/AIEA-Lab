% Facts
parent(john, mary).
parent(john, michael).
parent(mary, susan).
parent(mary, tom).
parent(michael, peter).
parent(michael, james).
parent(susan, alice).
parent(tom, david).

% Rule
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).    