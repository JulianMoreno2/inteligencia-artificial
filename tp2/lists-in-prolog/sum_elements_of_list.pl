sum([],0).

sum([X|Xs],T):-sum(Xs,T2),T is T2 + X.