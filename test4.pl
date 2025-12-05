% a) Every boy or girl is a child
child(X) :- boy(X).
child(X) :- girl(X).

% b) Every child gets a doll or a train or a lump of coal
gets(X, doll) :- child(X).
gets(X, train) :- child(X).
gets(X, coal) :- child(X).

% c) No boy gets any doll
:- boy(X), gets(X, doll).

% d) No child who is good gets any lump of coal
:- child(X), good(X), gets(X, coal).

% e) Jack is a boy
boy(jack).
