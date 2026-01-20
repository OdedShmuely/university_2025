"""
In this assignment you should interpolate the given function.
"""

import numpy as np
import time
import random


class Assignment1:
    def __init__(self):
        """
        Here goes any one time calculation that need to be made before 
        starting to interpolate arbitrary functions.
        """

        pass

    def interpolate(self, f: callable, a: float, b: float, n: int) -> callable:
        """
        Interpolate the function f in the closed range [a,b] using at most n 
        points. Your main objective is minimizing the interpolation error.
        Your secondary objective is minimizing the running time. 
        The assignment will be tested on variety of different functions with 
        large n values. 
        
        Interpolation error will be measured as the average absolute error at 
        2*n random points between a and b. See test_with_poly() below. 

        Note: It is forbidden to call f more than n times. 

        Note: This assignment can be solved trivially with running time O(n^2)
        or it can be solved with running time of O(n) with some preprocessing.
        **Accurate O(n) solutions will receive higher grades.** 
        
        Note: sometimes you can get very accurate solutions with only few points, 
        significantly less than n. 
        
        Parameters
        ----------
        f : callable. it is the given function
        a : float
            beginning of the interpolation range.
        b : float
            end of the interpolation range.
        n : int
            maximal number of points to use.

        Returns
        -------
        The interpolating function.
        """

        # checking edge case for n=1 --> return a line of the g(x) = f((a+b)/2) constant
        if n == 1:
            result = lambda x: f((a+b)/2)
            return result

        #create numpy arrays of X and Y to manipulate data faster
        arr_x_np = np.linspace(a,b,n)
        arr_y_np = np.array([f(x) for x in arr_x_np])
        dx = (b-a) / (n-1)
        num_of_curves = n-2
        use_of_log = 0
        current_y = arr_y_np

        # a function that recieves all the y points and calculatre the change of the changes
        def get_curv_sum(y_values):
            return np.sum(np.abs(np.diff(y_values,2)))

        min_curve = get_curv_sum(arr_y_np)

        if np.all(arr_y_np>0):
            logged_y_arr = np.log(arr_y_np)
            curve_logged_y = get_curv_sum(logged_y_arr)

            if curve_logged_y < min_curve:
                min_curve = curve_logged_y
                use_of_log += 1
                current_y = logged_y_arr

                if np.all(logged_y_arr>0):
                    logged_logged_y = np.log(logged_y_arr)
                    curve_lg_lg_y = get_curv_sum(logged_logged_y)

                    if curve_lg_lg_y < min_curve:
                        use_of_log += 1
                        current_y = logged_logged_y

        if num_of_curves < 1:
            complete_x = np.zeros(n)
        else:
            diag_main = np.full(num_of_curves, 4.0)
            diag_upper = np.full(num_of_curves - 1, 1.0)
            diag_lower = np.full(num_of_curves - 1, 1.0)
            #according to the formula, this is the b created from matrix A * vector x
            b_equation = (6 / dx**2) * (current_y[0:-2] - 2*current_y[1:-1] + current_y[2:])

            internal_x = self.solve_tridiagonal(diag_lower, diag_main, diag_upper, b_equation)
            complete_x = np.concatenate(([0], internal_x, [0]))


        # replace this line with your solution to pass the second test

        def result(x1):
            if x1<=a:
                value = current_y[0]
            elif x1>=b:
                value = current_y[-1]
            else:
                idx = int((x1 - a)/ dx)
                idx = min (idx,n-2)

                x_idx = arr_x_np[idx]
                x_nxt_idx = arr_x_np[idx+1]

                diff_curr = x1 - x_idx
                diff_nxt = x_nxt_idx - x1

                part1 = (complete_x[idx] * (diff_nxt ** 3) + complete_x[idx + 1] * (diff_curr ** 3)) / (6 * dx)
                part2 = (current_y[idx] - complete_x[idx] * (dx ** 2) / 6) * (diff_nxt / dx)
                part3 = (current_y[idx + 1] - complete_x[idx + 1] * (dx ** 2) / 6) * (diff_curr / dx)
                value = part1 + part2 + part3

            #get the logged arrays back to the original values
            if use_of_log == 0:
                return value
            elif use_of_log == 1:
                return np.exp(value)
            elif use_of_log == 2:
                return np.exp(np.exp(value))

        return np.vectorize(result)

    def solve_tridiagonal(self, lower_d, main_d, upper_d, b):
        n = len(main_d)
        lower = lower_d.copy()
        main = main_d.copy()
        upper = upper_d.copy()
        bb = b.copy()

        for i in range(1,n):
            helper = lower[i-1] / main[i-1]
            main[i] -= (helper*upper[i-1])
            bb[i] -= (helper* bb[i-1])

        t = np.zeros(n)
        t[-1] = bb[-1] / main[-1]

        for i in range (n-2,-1,-1):
            t[i] = (bb[i] - upper[i] * t[i+1]) / main[i]
        return t

##########################################################################


import unittest
from functionUtils import *
from tqdm import tqdm


class TestAssignment1(unittest.TestCase):

    def test_with_poly(self):
        T = time.time()

        ass1 = Assignment1()
        mean_err = 0

        d = 30
        for i in tqdm(range(100)):
            a = np.random.randn(d)

            f = np.poly1d(a)

            ff = ass1.interpolate(f, -10, 10, 100)

            xs = np.random.random(200)
            err = 0
            for x in xs:
                yy = ff(x)
                y = f(x)
                err += abs(y - yy)

            err = err / 200
            mean_err += err
        mean_err = mean_err / 100

        T = time.time() - T
        print(T)
        print(mean_err)

    def test_with_poly_restrict(self):
        ass1 = Assignment1()
        a = np.random.randn(5)
        f = RESTRICT_INVOCATIONS(10)(np.poly1d(a))
        ff = ass1.interpolate(f, -10, 10, 10)
        xs = np.random.random(20)
        for x in xs:
            yy = ff(x)

if __name__ == "__main__":
    unittest.main()
