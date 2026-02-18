"""
In this assignment you should fit a model function of your choice to data
that you sample from a given function.

The sampled data is very noisy so you should minimize the mean least squares
between the model you fit and the data points you sample.

During the testing of this assignment running time will be constrained. You
receive the maximal running time as an argument for the fitting method. You
must make sure that the fitting function returns at most 5 seconds after the
allowed running time elapses. If you take an iterative approach and know that
your iterations may take more than 1-2 seconds break out of any optimization
loops you have ahead of time.

Note: You are NOT allowed to use any numeric optimization libraries and tools
for solving this assignment.

"""

import numpy as np
import time
import random


class Assignment4:
    def __init__(self):
        """
        Here goes any one time calculation that need to be made before
        solving the assignment for specific functions.
        """

        pass

    def fit(self, f: callable, a: float, b: float, d:int, maxtime: float) -> callable:
        """
        Build a function that accurately fits the noisy data points sampled from
        some closed shape.

        Parameters
        ----------
        f : callable.
            A function which returns an approximate (noisy) Y value given X.
        a: float
            Start of the fitting range
        b: float
            End of the fitting range
        d: int
            The expected degree of a polynomial matching f
        maxtime : float
            This function returns after at most maxtime seconds.

        Returns
        -------
        a function:float->float that fits f between a and b
        """
        start_time = time.time()
        x_pylist = []
        y_pylist = []
        if maxtime > 1:
            safety_time = 0.5
        else:
            safety_time = 0.2 * maxtime

        max_samples = 10000
        cur_samples = 0
        n_chebyshev = min(3 * (d + 1), 100)

        for x in [a,b]:
            try:
                y = f(x)
                x_pylist.append(x)
                y_pylist.append(y)
                cur_samples += 1
            except:
                pass
        for i in range(n_chebyshev):
            if time.time() - start_time > (maxtime - safety_time):
                break

            alpha = (2 * i + 1) * np.pi / (2* n_chebyshev)
            x = (a + b) / 2 + (a + b) /2 * np.cos(alpha)

            try:
                y = f(x)
                x_pylist.append(x)
                y_pylist.append(y)
                cur_samples +=1
            except:
                pass

        while True:
            current_time = time.time()
            if (current_time - start_time) > (maxtime - safety_time) or cur_samples >= max_samples:
                break

            x = random.uniform(a, b)

            try:
                y = f(x)
                x_pylist.append(x)
                y_pylist.append(y)
                cur_samples += 1
            except Exception:
                pass

        #if tthe max time is small and there is no data to work with, return a function so the code won't crash
        if cur_samples == 0:
            return lambda x2: 0.0

        try:
            # start working with numpy
            x_np_arr = np.array(x_pylist)
            y_np_arr = np.array(y_pylist)

            # composing the matrix A from the x's and the powers:
            power_arr = np.arange(d,-1,-1)
            A = x_np_arr[:, np.newaxis] ** power_arr

            # making the matrix compatible and squared so we can work with it on both sides
            # the form created is like At * A * vector p = At * vector b represented by the y list
            AtA = A.T @ A
            Aty = A.T @ y_np_arr

            coefficients = self.matrix_solution(AtA, Aty)

            answer = np.poly1d(coefficients)
            return answer

        except Exception:
            if len(y_pylist) > 0:
                mean_y = np.mean(y_pylist)
            else:
                mean_y = 0.0
            return lambda x2: mean_y


    def matrix_solution(self, A, b):
        """
        a function to help me find a solution to the equation in the form of A * x = b
        using the values:
        :param A: np.array, matrix A multiplied by transposed A
        :param b: np.array, vector of y values multiplied by transposed A
        :return: np.array, coefficients, vector solution to the matrix
        """

        M = np.array(A, dtype=float)
        v = np.array(b, dtype=float)
        n = len(v)

        # pre-solution step to arrange the maximal values the highest
        for i in range(n):
            pivot_idx = np.argmax(np.abs(M[i:, i])) + i
            if i != pivot_idx:
                M[[i,pivot_idx]] = M[[pivot_idx,i]]
                v[[i,pivot_idx]] = v[[pivot_idx,i]]

            pivot = M[i,i]
            if abs(pivot) < 1e-11:
                continue

            M[i] = M[i] / pivot
            v[i] = v[i] / pivot

            for j in range(i+1,n):
                divisor = M[j,i]
                M[j] -= divisor * M[i]
                v[j] -= divisor * v[i]
        result = np.zeros(n)
        for i in range(n-1,-1,-1):
            sum_allx = np.dot(M[i, i+1:], result[i+1:])
            result[i] = v[i] - sum_allx

        return result
##########################################################################


import unittest
from sampleFunctions import *
from tqdm import tqdm


class TestAssignment4(unittest.TestCase):

    def test_return(self):
        f = NOISY(0.01)(poly(1,1,1))
        ass4 = Assignment4()
        T = time.time()
        shape = ass4.fit(f=f, a=0, b=1, d=10, maxtime=5)
        T = time.time() - T
        self.assertLessEqual(T, 5)

    def test_delay(self):
        f = DELAYED(7)(NOISY(0.01)(poly(1,1,1)))

        ass4 = Assignment4()
        T = time.time()
        shape = ass4.fit(f=f, a=0, b=1, d=10, maxtime=5)
        T = time.time() - T
        self.assertGreaterEqual(T, 5)

    def test_err(self):
        f = poly(1,1,1)
        nf = NOISY(1)(f)
        ass4 = Assignment4()
        T = time.time()
        ff = ass4.fit(f=nf, a=0, b=1, d=10, maxtime=5)
        T = time.time() - T
        mse=0
        for x in np.linspace(0,1,1000):
            self.assertNotEqual(f(x), nf(x))
            mse+= (f(x)-ff(x))**2
        mse = mse/1000
        print(mse)






if __name__ == "__main__":
    unittest.main()