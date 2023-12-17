

female(alice).
female(emily).
female(lily).
female(sophia).
male(jack).
male(mason).
male(owen).
male(noah).
% parent(X, Y) means X is the parent of Y , x=parent, y=child
parent(alice, mason).
parent(jack, mason).
parent(jack, lily).
parent(mason, sophia).
parent(mason, owen).
parent(lily, noah).
parent(mason, noah).
parent(lily, sophia).
parent(alice, emily).
% Rules
mother(X, Y):- parent(X, Y), female(X).
father(X, Y):- parent(X, Y), male(X).

haschild(X):- parent(X, _).

sister(X, Y):- parent(Z, X), parent(Z, Y), female(X), X \== Y.
brother(X, Y):- parent(Z, X), parent(Z, Y), male(X), X \== Y.
sibling(X,Y):- parent(Z,X),parent(Z,Y),X\==Y.
grandfather(X, Y) :- father(X, Z), parent(Z, Y).
