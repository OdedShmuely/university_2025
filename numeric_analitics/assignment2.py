"""
In this assignment you should find the intersection points for two functions.
"""

import numpy as np
import time
import random
from collections.abc import Iterable


class Assignment2:
    def __init__(self):
        """
        Here goes any one time calculation that need to be made before 
        solving the assignment for specific functions. 
        """

        self.interList = []


    def _mixBiSecant (self, f, x0, x1, y0, y1, maxerr):
        '''
        finding the root using a mix of secant method and bisection method
        :param f: short for absulute f1-f2
        :param x0: left limit
        :param x1:right limit
        :param y0:f value for x0
        :param y1:f value for x1
        :param maxerr: the error
        :return: x of the root in the section between x0 to x1
        '''
        #return the x if y is a root
        if abs(y0) < maxerr: return x0
        if abs(y1) < maxerr: return x1

        #fo 50 times or untill i find a root
        for i in range(50):
            try:
                if abs(y1-y0) < 1e-11:
                    next_x = (x0+x1)/2
                else:
                    next_x = x1 - y1 * (x1-x0) / (y1-y0)
            except ArithmeticError:
                next_x = (x0+x1)/2

            #next x is inborder --> secant | else --> bisection
            if not (min(x0,x1) < next_x < max(x0,x1)):
                next_x = (x0 + x1) / 2

            next_y = f(next_x)
            if abs(next_y) <= maxerr:  # found a root, return the next x var
                return next_x

            if np.sign(y0) != np.sign(next_y):
                x1 = next_x
                y1 = next_y
            else:
                x0 = next_x
                y0 = next_y

        return None


    def intersections(self, f1: callable, f2: callable, a: float, b: float, maxerr=0.001) -> Iterable:
        """
        Find as many intersection points as you can. 
        
        This function may not work correctly if there is infinite number of
        intersection points. 


        Parameters
        ----------
        f1 : callable
            the first given function
        f2 : callable
            the second given function
        a : float
            beginning of the interpolation range.
        b : float
            end of the interpolation range.
        maxerr : float
            An upper bound on the difference between the
            function values at the approximate intersection points.


        Returns
        -------
        X : iterable of approximate intersection Xs such that for each x in X:
            |f1(x)-f2(x)|<=maxerr.

        """
        self.interList = []
        def f(x):
            return f1(x) - f2(x)

        #divide the section to 2000 mini sections in a np array and fill the y arrray whith the function values
        x = np.linspace(a, b, 2000)
        try:
            y = f1(x) - f2(x)
        except:
            y = np.array([f(num) for num in x])

        #check if there are values that primarly lower than the maxerr value (absulute 0 that wont be cought in the algorithm)
        abs_zeros = np.where(np.abs(y) < maxerr)[0]
        for idx in abs_zeros:
            self.interList.append(x[idx])

        #call the mixbisecant on the opposite signs values in y
        opposite_signs_arr = np.where(np.sign(y[:-1]) * np.sign(y[1:]) < 0)[0]
        for idx in opposite_signs_arr:
            root = self._mixBiSecant(f, x[idx], x[idx+1], y[idx], y[idx+1], maxerr)
            if root is not None:
                self.interList.append(root)

        if not self.interList:
            return []

        return self.interList


##########################################################################


import unittest
from sampleFunctions import *
from tqdm import tqdm


class TestAssignment2(unittest.TestCase):

    def test_sqr(self):

        ass2 = Assignment2()

        f1 = np.poly1d([-1, 0, 1])
        f2 = np.poly1d([1, 0, -1])

        X = ass2.intersections(f1, f2, -1, 1, maxerr=0.001)

        for x in X:
            self.assertGreaterEqual(0.001, abs(f1(x) - f2(x)))

    def test_poly(self):

        ass2 = Assignment2()

        f1, f2 = randomIntersectingPolynomials(10)

        X = ass2.intersections(f1, f2, -1, 1, maxerr=0.001)

        for x in X:
            self.assertGreaterEqual(0.001, abs(f1(x) - f2(x)))


if __name__ == "__main__":
    unittest.main()
