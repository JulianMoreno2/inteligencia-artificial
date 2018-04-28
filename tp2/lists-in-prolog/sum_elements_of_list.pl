sum([], 0).
sum([X|Xs], T):-sum(Xs, T1),T is T1 + X.
