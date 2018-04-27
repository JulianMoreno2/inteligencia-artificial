count([],0). 
count([X|Xs], T) :-count(Xs, T1),(number(X) -> T is T1 + 1;  T = T1).