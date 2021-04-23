# highs-ipm-debugging

To run the script, first decompress the datasets
```
gzip -d A.csv.gz
gzip -d b.csv.gz
```
Then run
```
./run_solver.py
```
A requirements file is in this repository so you can create a virtual environment with the version of SciPy I am using. I am running Python 3.8.5 on Ubuntu 20.04.2 LTS.

## Example
```
(.ve3) $:~/highs-ipm-debugging$ gzip -d A.csv.gz 
(.ve3) $:~/highs-ipm-debugging$ gzip -d b.csv.gz 
(.ve3) $:~/highs-ipm-debugging$ ./run_solver.py 
n_a: 10009
n_u: 8448
./run_solver.py:27: OptimizeWarning: Sparse constraint matrix detected; setting 'sparse':True.
  res = linprog(
./run_solver.py:27: OptimizeWarning: Unknown solver options: sparse
  res = linprog(
Presolve : Reductions: rows 7846(-12172); columns 12371(-6086); elements 56868(-12172)
INFO   : Solving the presolved LP
INFO   : IPX model has 7846 rows, 12371 columns and 56868 nonzeros
IPX version 1.0
Input
    Number of variables:                                12371
    Number of free variables:                           0
    Number of constraints:                              7846
    Number of equality constraints:                     0
    Number of matrix entries:                           56868
    Matrix range:                                       [1e+00, 1e+00]
    RHS range:                                          [1e+00, 7e+03]
    Objective range:                                    [1e+00, 1e+00]
    Bounds range:                                       [0e+00, 0e+00]
Preprocessing
    Dualized model:                                     no
    Number of dense columns:                            0
    Range of scaling factors:                           [1.00e+00, 1.00e+00]
Interior Point Solve
 Iter     P.res    D.res            P.obj           D.obj        mu     Time
   0   1.77e+03 1.60e+00   0.00000000e+00 -5.88217119e-09  3.19e+03       0s
   1   1.11e+02 6.88e-02   4.50833398e+06 -2.63519598e+05  3.79e+02       0s
   2   2.45e+01 2.24e-02   1.38432873e+06 -1.86162397e+05  1.01e+02       0s
   3   2.67e+00 1.05e-02   4.78113499e+05 -1.19571205e+05  3.23e+01       0s
   4   3.35e-01 4.69e-03   1.64393395e+05 -6.37697332e+04  1.17e+01       0s
   5   6.04e-02 2.01e-03   6.82218365e+04 -3.13569555e+04  5.00e+00       0s
 Constructing starting basis...
   6   1.65e-02 7.92e-04   3.05842987e+04 -1.44062544e+04  2.24e+00       0s
   7   5.06e-03 3.07e-04   1.42213368e+04 -6.69349551e+03  1.04e+00       0s
   8   1.67e-03 1.00e-04   6.63983531e+03 -2.57683167e+03  4.58e-01       1s
   9   7.77e-04 4.66e-05   4.15739611e+03 -1.33422740e+03  2.72e-01       1s
  10   4.37e-04 1.68e-05   3.03407409e+03 -5.25156717e+02  1.76e-01       2s
  11   2.39e-04 5.79e-06   2.12239636e+03 -9.23362726e+01  1.10e-01       2s
  12   1.20e-04 2.24e-06   1.63597642e+03  2.38494825e+01  7.98e-02       2s
  13   7.62e-05 6.04e-07   1.36921087e+03  1.67741111e+02  5.95e-02       2s
  14   1.66e-05 2.37e-07   8.45993658e+02  2.71126453e+02  2.84e-02       2s
  15   1.18e-06 3.91e-08   5.09965199e+02  4.25157791e+02  4.20e-03       2s
  16   2.62e-08 7.46e-09   4.68188913e+02  4.58888839e+02  4.60e-04       2s
  17   1.95e-12 2.34e-09   4.67047016e+02  4.64430384e+02  1.29e-04       2s
  18   1.60e-12 1.13e-10   4.67079842e+02  4.66823744e+02  1.27e-05       2s
  19   1.91e-12 2.29e-11   4.67000143e+02  4.66964022e+02  1.79e-06       3s
  20   1.25e-12 5.64e-12   4.67000131e+02  4.66991064e+02  4.49e-07       3s
  21   1.24e-12 1.39e-12   4.67000103e+02  4.66997753e+02  1.16e-07       3s
  22   1.74e-12 2.59e-13   4.67000452e+02  4.66999333e+02  5.53e-08       3s
  23   1.78e-12 3.28e-14   4.67000006e+02  4.66999916e+02  4.44e-09       3s
  24   2.03e-12 6.91e-15   4.67000002e+02  4.66999983e+02  9.49e-10       3s
  25*  1.32e-12 1.78e-15   4.67000000e+02  4.66999996e+02  2.35e-10       3s
Crossover
    Primal residual before push phase:                  4.66e-10
    Dual residual before push phase:                    1.16e-08
    Number of dual pushes required:                     3914
    Number of primal pushes required:                   4198
Summary
    Runtime:                                            4.95s
    Status interior point solve:                        optimal
    Status crossover:                                   failed
    objective value:                                    4.67000000e+02
    interior solution primal residual (abs/rel):        2.81e-10 / 4.06e-14
    interior solution dual residual (abs/rel):          4.39e-10 / 2.20e-10
    interior solution objective gap (abs/rel):          3.97e-06 / 8.49e-09
WARNING: Ipx: Stopped
INFO   : Ipx: IPM       optimal
ERROR  : Ipx: Crossover failed
Status: 4
Message: HiGHS Status Code 0: HighsModelStatusNOTSET
Iterations: 0
No solutions available: True
```
