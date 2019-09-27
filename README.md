# A_Star_Search

The A* Search Algorithm is an informed search algorithm.

An informed search algorithm is a search algorithm that already knows the layout of the graph or map from beginning to end and goes through looking for the most efficient path to that desired end goal.

It is commonly used in applications such as video games and online learning

It follows the equation: F(n) = G(n) + H(n)

n = the next step to be taken

G(n) = the total cost of the path from the start to the current position.

H(n) = the estimated cost from the current position on the graph to the end point

It is nearly impossible to define a specific time complexity for this algorithm due to the fact that it relies on the heuristic 
