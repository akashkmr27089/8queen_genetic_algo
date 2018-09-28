# Solving 8queen Problem using Genetic Algorithm
In this Program, we will try to solve 8 queen problem using genetic Algorithm 

8 queen problem. The eight queens problem is the problem of placing eight queens on an 8×8 chessboard such that none of them attack one another (no two are in the same row, column, or diagonal). We will try to solve the problem of Placing queens using Genetic Algorithm.  

# Program Architecture:
8 queen Problem is represented as numpy array of 8*8. Initially all 8 queens are placed randomly one at each row uniquely. For solving this Problem, we will be using complete-state formulation, where each state has 8 queens on the board , one per column. 


# Classes Used :
1. Play Class():
	Play Class is used initialise the data_arrays:
	
	Variable used :
		
		a. box -> Box variable will store the postion of queens in the board. The whole board is zeros matrix and contains 1 in the postion of queens
		
		b. queen_pos -> vector of 8 dimention -- this will store the position of queens in the board (value range 0 - 7)

		c. huristic_score --> used to store the fitness score -- where the high fitness score represents more close to the goal (max : 28)

		d. attacking_paris --> will contains the conflicting queen information

# Huristic Functions as fitness function:

1. In huristic function h1, the fitness depends on the number of non conflicting Queen. For this problem ,for each queen , we need to cheack both the diagonal , vertical and horizontal with respect ot the given queen and find the value from fitness. This in turn will be used to calculate probability for selection in genetic algorithm for cross breeding populations.


# Genitic Algorithm

Coming Soon
