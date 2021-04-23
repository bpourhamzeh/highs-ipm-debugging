#!/usr/bin/env python3
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import csc_matrix

LINPROG_METHOD = "highs-ipm"
FEASIBILITY_TOL = 1e-7
OPTIMALITY_TOL = 1e-8


def load(fn_A="A.csv.gz", fn_b="b.csv.gz"):
    A = csc_matrix(np.loadtxt(fn_A, dtype=np.int8, delimiter=","))
    b = np.loadtxt(fn_b, dtype=np.int32, delimiter=",").flatten()
    
    n_a = A.shape[0] // 2
    n_u = A.shape[1] - n_a
    print('n_a:', n_a)
    print('n_u:', n_u)
    c = np.hstack((np.ones(n_a, dtype=np.int8), np.zeros(n_u, dtype=np.int8)))

    return A, b, c


if __name__ == "__main__":
    A, b, c = load()
    res = linprog(
        c,
        A_ub=A,
        b_ub=b,
        method=LINPROG_METHOD,
        options={
            "disp": True,
            "dual_feasibility_tolerance": FEASIBILITY_TOL,
            "primal_feasibility_tolerance": FEASIBILITY_TOL,
            "ipm_optimality_tolerance": OPTIMALITY_TOL,
        },
    )
    print('Status:', res.status)
    print('Message:', res.message)
    print('Iterations:', res.nit)
    print('No solutions available:', res.x is None)

