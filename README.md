A function that returns the sum of the Nth row of a Pascal triangle. The function should take an integer N as the argument. 
N is for the number of rows.

In mathematics, Pascal's triangle is a triangular array of the binomial coefficients. Below are the first few rows of the Pascal's triangle:

                    1
                1       1
            1       2       1
        1       3       3      1
    1       4       6      4      1
1       5      10      10      5      1
The numbers on the edges of the triangle are always 1. Each of the remaining numbers are the sum of the two numbers that appear immediately above it.

The sum of the 5th row, for example, is 1 + 4 + 6 + 4 + 1 = 16.

Input
The input will contain one integer N (0 < N <= 30).

Output
Print the sum of the Nth row of Pascal's triangle.

Sample
Input	  |    Output
5       |    16
8       |    128
30      |    536870912

If you finish within the time limit, extra credit will be given for the creation of unit tests for the above sample cases.
Extra credit will also be given for handling edge cases.
