live_in_house(agatha).

live_in_house(butcher).

live_in_house(charles).

hate(charles,X):-not(hate(agatha,X)),live_in_house(X).

hate(agatha,X):-not(X==butcher),live_in_house(X).

hate(butcher,X):-not(X==butcher),live_in_house(X).

more_reach_than(X,agatha):-not(hate(butcher,X)),live_in_house(X).

murder(X,agatha):-hate(X,agatha),live_in_house(X),not(more_reach_than(X,agatha)).