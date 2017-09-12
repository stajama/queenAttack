A simple program to identify if a given piece or location on a chess board of arbitrary size is in danger of attack from an opposing queen. 

Inputs: squaresUnderQueenAttack(n, queens, queries)

n = number of queries,
queens = nested list of lists of queen locations, in x, y coordinates 
queries = nested list of lists of query positions, in x, y coordinates

Returns: a list of boolean values; True if corresponding location is vulnerable.