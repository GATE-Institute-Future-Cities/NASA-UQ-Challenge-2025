# Monotonicity experiment inputs

To find the corresponding outputs look in Outputs/Monotonicity experiments for the files with the same name as the .txt files here.
A few things to consider:

1. X1 controls intensity of the signal - it does not change over time, it is seed invariant, and monotone (i.e. higher value of x1 results in higher value for the time series).
2. X2 controls randomness in the signal - it changes over time, it is seed dependent and non-monotone. For the purpose of most experiments, X2 is removed by setting it to 0.
3. X3-X8 have an effect on the intensity - do not change over time, seed invariant, some are monotone others not. (for more detail check monotonicity.ipynb).

4. the seed parameter is can take an integer value in the range [1, 2^31-1].

5. Xi cannot be negative or above 1.

For more detail about the different outputs check the readme in Outputs.
