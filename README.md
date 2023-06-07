# The 8 puzzle problem 

# Input - Enter the initial and final configuration in the form of a 3x3 matrix
         with the empty space or blank as zero
        
# Output - If the problem is not solvable, the programme will print "Not Possible", otherwise, it'll print all the steps 
         if the problem is solvable in less than 10 steps, otherwise it'll print the first 10 steps and will print 
         "The given problem can be solved but will require more than 10 steps.".

# Explanation of the logic and code :-

The programme gives the step-by-step solution to solving the 8 puzzle problem.
The input takes the initial and final configuration. I'm taking the input by "list(map(int,input().split())) for i in range(3)".
Here, it takes the input as a string and then splits it according to the whitespaces and returns a list of strings. Then, it is
changed into a list of integers. This process is done 3 times.

We are required to find if the problem is solvable, if not, the programme will print "Not Possible", otherwise, it'll 
print all the steps if the problem is solvable in less than 10 steps, otherwise it'll print the first 10 steps and will
print "The given problem can be solved but will require more than 10 steps.".

I've created two functions, one is, swap function and the other is, possible function. The swap function swaps the empty tile
and any other tile which can be swapped. Possible function checks if a swap is possible, a swap is possible if the tile that is
going to be swapped is the position of that tile in the final configuration, otherwise, it is not. If we have a possible
swap, we do the swap and then reduce the misplaced by 1, since we got a tile into it's place. If we don't find any swap,
then we have some default swaps which are followed.

I've imported a python library to store the updated initial configuration and later when we swap and if we get the same configuration then we
reverse the swap and then do a new swap. Otherwise, we store the configuration and we continue. We are using deep copy because we don't want the
copy of the current initial configuration to change if we change initial configuration later.

After taking the input, first, I need to determine whether the problem is solvable or not by using the inversion count. For
this, I've taken the matrix as a list of integers and then I calculated the inversion count. If the parity of the inversion 
counts of the initial and final configuration are not equal, then the problem cannot be solved, then, I printed that the 
problem cannot be solved. Otherwise, the problem can be solved, then, I ran the possible function 10 times and printed every 
the changed or updated configuration. If we can reach the final configuration within 10 steps, then, I printed "Final Configuration"
and printed the number of steps it took. If we don't reach the final configuration within 10 steps, then I've printed that
the problem is solvable but it'll take more than 10 steps.
