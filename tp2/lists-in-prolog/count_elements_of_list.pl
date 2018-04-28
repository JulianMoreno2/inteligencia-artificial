count([], 0).
count([X|Xs], T):-count(Xs, T1),T is T1 + 1.
