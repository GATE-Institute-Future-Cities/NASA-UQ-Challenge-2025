# Monotonicity experiment outputs

To find the corresponding inputs look in Inputs/Monotonicity experiments for the files with the same name as the .csv files here.
A few things to consider:

1.  the datasets with 'X1_Xi' are generated using the following inputs: for every possible pair (x1, xi) are generated 20 samples. The samples are ordered based on the x1 value, and then based on xi value. x1 and xi change between 0.1 and 1.0 with step 0.1 (0.1, 0.2, 0.3, etc). All other input parameters are set to 0. For more info check the corresponding inputs in Inputs folder.

2. the datasets with 'X1_Xi_0_1' are generated using the following inputs: for every possible pair (x1, xi) are generated 20 samples. The samples are ordered based on the x1 value, and then based on xi value. x1 and xi change between 0.1 and 1.0 with step 0.1 (0.1, 0.2, 0.3, etc). All other input parameters are set to 0.1 (except x2 which is set 0). For more info check the corresponding inputs in Inputs folder.

3. If x1 and x2 are 0, then the system produces only 0s no matter the other input parameters.

4. the datasets 'X1' and 'X2' are generated only by changing x1 and x2, respectively.

5. The values for y1,y2,y3 are in the interval [0, 3.35] while the interval for y4-y6 is R+. 

6. For the notebook results check 'monotonicity.ipynb'.

For more detail about the different inputs check the readme in Inputs.

