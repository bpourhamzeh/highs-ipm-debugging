# highs-ipm-debugging

To run the script, execute
```
./run_solver.py
```
A requirements file is in this repository so you can create a virtual environment with the version of SciPy I am using. I am running Python 3.8.5 on Ubuntu 20.04.2 LTS.

## Example
```
(.ve3) ubuntu@desktop:~/highs-ipm-debugging$ ./run_solver.py 
Loading files: data/A3.csv.gz data/b3.csv.gz
n_a: 9984
n_u: 40909
Using options:
 {
    "disp": true,
    "dual_feasibility_tolerance": 1e-06,
    "primal_feasibility_tolerance": 1e-06,
    "ipm_optimality_tolerance": 1e-07
}
./run_solver.py:36: OptimizeWarning: Sparse constraint matrix detected; setting 'sparse':True.
  res = linprog(
./run_solver.py:36: OptimizeWarning: Unknown solver options: sparse
  res = linprog(
Presolve : Reductions: rows 15500(-4468); columns 48659(-2234); elements 255668(-4468)
INFO   : Solving the presolved LP
INFO   : IPX model has 15500 rows, 48659 columns and 255668 nonzeros
IPX version 1.0
Input
    Number of variables:                                48659
    Number of free variables:                           0
    Number of constraints:                              15500
    Number of equality constraints:                     0
    Number of matrix entries:                           255668
    Matrix range:                                       [1e+00, 1e+00]
    RHS range:                                          [1e+00, 1e+04]
    Objective range:                                    [1e+00, 1e+00]
    Bounds range:                                       [0e+00, 0e+00]
Preprocessing
    Dualized model:                                     no
    Number of dense columns:                            0
    Range of scaling factors:                           [1.00e+00, 1.00e+00]
Interior Point Solve
 Iter     P.res    D.res            P.obj           D.obj        mu     Time
   0   1.78e+03 1.56e+00   0.00000000e+00 -8.09310592e-08  3.00e+03       0s
   1   8.75e+01 7.56e-02   8.96112151e+06 -8.18668050e+05  2.83e+02       0s
   2   2.18e+01 3.42e-02   3.10351097e+06 -6.30322257e+05  8.59e+01       0s
   3   3.93e+00 1.56e-02   1.23131101e+06 -4.23855169e+05  3.06e+01       0s
   4   8.18e-01 6.67e-03   5.65399325e+05 -2.63250251e+05  1.38e+01       0s
   5   2.12e-01 2.63e-03   1.96068277e+05 -1.45101402e+05  5.51e+00       0s
   6   7.45e-02 9.21e-04   8.03161461e+04 -7.31560299e+04  2.44e+00       1s
 Constructing starting basis...
   7   4.13e-02 1.48e-04   5.24256471e+04 -2.83560769e+04  1.27e+00       5s
   8   2.78e-03 6.16e-05   1.04094897e+04 -1.75710738e+04  4.37e-01       5s
   9   6.87e-04 1.10e-05   2.98555950e+03 -3.57779671e+03  1.03e-01       6s
  10   1.87e-04 1.24e-06   9.07900007e+02 -6.03495254e+02  2.36e-02       8s
  11   1.67e-05 1.24e-12   1.40115087e+02 -1.14922511e+02  3.98e-03       8s
  12   6.23e-06 3.68e-13   5.24368550e+01 -3.43295094e+01  1.35e-03       9s
  13   2.55e-06 1.32e-13   2.14833649e+01 -1.23242331e+01  5.27e-04       9s
  14   1.43e-06 3.02e-14   1.35171927e+01 -7.26993198e+00  3.24e-04      10s
  15   1.15e-11 4.46e-15   7.46657019e-04 -1.01157017e+00  1.58e-05      10s
  16   1.35e-11 1.46e-15   2.55801425e-03 -2.62549779e-01  4.13e-06      11s
  17   8.43e-12 4.66e-16   2.88203153e-03 -2.07193274e-02  3.68e-07      11s
  18   1.07e-11 4.12e-16   6.82223214e-04 -5.99210151e-03  1.04e-07      12s
  19   6.62e-12 3.65e-16   2.39604108e-04 -1.33379680e-03  2.45e-08      12s
  20   6.26e-12 4.76e-16   1.20057859e-04 -4.55390040e-04  8.97e-09      13s
  21   6.88e-12 4.72e-16   9.11901044e-05 -9.63403198e-05  3.01e-09      14s
  22   4.25e-12 3.92e-16   2.71614116e-05 -1.53979882e-05  9.33e-10      22s
  23   2.97e-12 3.85e-16   3.02081744e-06 -5.92251490e-07  1.12e-10      28s
  24*  1.61e-12 3.62e-16   8.89449319e-09 -5.12743118e-08  2.62e-12      29s
Crossover
    Primal residual before push phase:                  1.82e-12
    Dual residual before push phase:                    1.19e-10
    Number of dual pushes required:                     7750
    Number of primal pushes required:                   33159
    27638 primal pushes remaining (   5322 pivots)
    22161 primal pushes remaining (  10682 pivots)
    16921 primal pushes remaining (  15775 pivots)
Summary
    Runtime:                                            45.11s
    Status interior point solve:                        imprecise
    Status crossover:                                   failed
    objective value:                                    6.72195793e-09
    interior solution primal residual (abs/rel):        2.76e-12 / 2.55e-16
    interior solution dual residual (abs/rel):          1.10e-10 / 5.48e-11
    interior solution objective gap (abs/rel):          2.84e-07 / 2.84e-07
WARNING: Ipx: Stopped
WARNING: Ipx: IPM       imprecise
ERROR  : Ipx: Crossover failed
Status: 4
Message: HiGHS Status Code 0: HighsModelStatusNOTSET
Iterations: 0
No solutions available: True
```

## Data legend
| File number | Description |
| ----------- | ----------- |
| 1           | highs-ipm: Crossover failed; highs-ds: successful |
| 2           | highs-ipm: Infinite loop with default tolerances; success with lowered tolerances |
| 3           | highs-ipm: Crossover failed when feasibility_tolerance=1e-6 and optimality_tolerance=1e-7, success when feasibility_tolerance=1e-7 and optimality_tolerance=1e-8 |
| 4           | highs-ipm: Crossover failed, all rows of A are inearly independent |
