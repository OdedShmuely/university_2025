"""
In this assignment you should find the area enclosed between the two given functions.
The rightmost and the leftmost x values for the integration are the rightmost and
the leftmost intersection points of the two functions.

The functions for the numeric answers are specified in MOODLE.

This assignment is more complicated than Assignment1 and Assignment2 because:
    1. You should work with float32 precision only (in all calculations) and minimize the floating point errors.
    2. You have the freedom to choose how to calculate the area between the two functions.
    3. The functions may intersect multiple times. Here is an example:
        https://www.wolframalpha.com/input/?i=area+between+the+curves+y%3D1-2x%5E2%2Bx%5E3+and+y%3Dx
    4. Some of the functions are hard to integrate accurately.
       You should explain why in one of the theoretical questions in MOODLE.

"""

import numpy as np
import time
import random
from assignment2 import Assignment2


class Assignment3:
    def __init__(self):
        self._gl_cache = {} #gl stands for: Gauss-Legendre

    def _get_gl_nodes(self, n):
        """Returns cached Gauss-Legendre nodes and weights for n points."""
        if n not in self._gl_cache:
            self._gl_cache[n] = np.polynomial.legendre.leggauss(n)
        return self._gl_cache[n]

    def integrate(self, f: callable, a: float, b: float, n: int) -> np.float32:
        """
        Integrate f over [a,b]
        Returns np.float32.
        """
        if a == b or n < 1:
            return np.float32(0.0)

        flip = False
        if a > b:
            a, b = b, a
            flip = True

        a = np.float32(a)
        b = np.float32(b)

        if n == 1:
            mid = np.float32((a + b) * 0.5)
            return np.float32((b - a) * f(mid)) * np.float32(-1 if flip else 1)

        if n == 2:
            fa = np.float32(f(a))
            fb = np.float32(f(b))
            result = np.float32((b - a) * 0.5 * (fa + fb))
            return np.float32(-result if flip else result)

        if n <= 4:
            # Small n: use all points for GL, skip detection
            nodes, weights = self._get_gl_nodes(n)
            half = np.float32((b - a) * 0.5)
            mid  = np.float32((a + b) * 0.5)
            xpts = (half * nodes + mid).astype(np.float32)
            yvals = np.asarray(f(xpts), dtype=np.float32)
            result = np.float32(np.sum(weights.astype(np.float32) * yvals * half))
            return np.float32(-result if flip else result)

        # Handle functions that don't vectorize (return scalar for array input)
        try:
            endpoints = np.array([a, b], dtype=np.float32)
            raw = np.asarray(f(endpoints), dtype=np.float32)
            raw = np.atleast_1d(raw)
            if raw.shape[0] >= 2:
                fa, fb = float(raw[0]), float(raw[1])
            else:
                fa = float(np.asarray(f(a), dtype=np.float32).flat[0])
                fb = float(np.asarray(f(b), dtype=np.float32).flat[0])
        except Exception:
            fa = float(np.asarray(f(a), dtype=np.float32).flat[0])
            fb = float(np.asarray(f(b), dtype=np.float32).flat[0])

        # using log or not
        use_log  = False
        log_power = 1.0

        if a > 0 and b > 0:
            fa_abs = max(abs(fa), 1e-30)
            fb_abs = max(abs(fb), 1e-30)
            if fa_abs > 1e-20 and fb_abs > 1e-20:
                magnitude_gap = abs(np.log10(fa_abs / fb_abs))
                if magnitude_gap > 3.0:
                    use_log = True
                    if magnitude_gap > 30:
                        log_power = 3.8
                    elif magnitude_gap > 20:
                        log_power = 3.5
                    elif magnitude_gap > 10:
                        log_power = 3.0
                    else:
                        log_power = 2.5

        n_quad = n - 2
        nodes, weights = self._get_gl_nodes(n_quad)
        weights32 = weights.astype(np.float32)

        if use_log:
            # x(s) = a * (b/a)^(s^p) and s is in [0,1] and GL nodes from [-1,1] to [0,1]
            s = ((nodes + 1.0) * 0.5)
            s_p = np.power(s, log_power)
            ratio = float(b / a)
            xpts = np.float32(a * np.power(ratio, s_p))
            # using Jacobian wich is: dx/d(GL_node) = x*ln(ratio)*p*s^(p-1) / 2
            ln_ratio = np.log(ratio)
            jacobian = np.float32(
                xpts * ln_ratio * log_power * np.power(s, log_power - 1.0) * 0.5
            )
        else:
            # Standard linear mapping from gl nodes [-1,1] to [a,b]
            half = np.float32((b - a) * 0.5)
            mid = np.float32((a + b) * 0.5)
            xpts = (half * nodes + mid).astype(np.float32)
            jacobian = half

        yvals = np.asarray(f(xpts), dtype=np.float32)
        integrand = yvals * jacobian

        # Normalize by the largest value before summing to avoid overflow
        peak = np.float32(np.max(np.abs(integrand)))
        if peak > np.float32(1.0):
            normed = integrand / peak
            total  = np.float32(peak * np.sum(weights32 * normed))
        else:
            total = np.float32(np.sum(weights32 * integrand))

        # stick to float32 range
        MAX32 = np.float32(3.4e38)
        if abs(total) > MAX32:
            total = np.float32(np.sign(total)) * MAX32

        return np.float32(-total if flip else total)

    def areabetween(self, f1: callable, f2: callable) -> np.float32:
        """
        find the area enclosed between two functions: f1 and f2
        searching intersections in [1, 100] and include them in consideration.
        returns - np.float32
        the area between the functions
        """
        def abs_diff(x):
            """
            Helper function
            Calculates the absolute distance between the two functions
            """
            try:
                result = np.abs(np.asarray(f1(x), dtype=np.float32) -
                                np.asarray(f2(x), dtype=np.float32))
                if np.asarray(result).shape == np.asarray(x).shape:
                    return result
                raise ValueError("shape mismatch")
            except Exception:
                if hasattr(x, '__iter__'):
                    return np.array([abs(float(f1(xi)) - float(f2(xi)))
                                     for xi in x], dtype=np.float32)
                return np.float32(abs(float(f1(x)) - float(f2(x))))

        ass2 = Assignment2()
        raw_intersections = ass2.intersections(f1, f2, 1, 100, maxerr=0.001)
        intersections = sorted(set(np.float32(x) for x in raw_intersections))

        if len(intersections) < 2:
            return np.float32(np.nan)


        N_PER_SEGMENT = 111

        total_area = np.float32(0.0)
        for i in range(len(intersections) - 1):
            left  = np.float32(intersections[i])
            right = np.float32(intersections[i + 1])
            if right - left < np.float32(1e-6):
                continue
            seg = self.integrate(abs_diff, left, right, N_PER_SEGMENT)
            total_area = np.float32(total_area + abs(seg))

        return np.float32(total_area)



##########################################################################


import unittest
from sampleFunctions import *


class TestAssignment3(unittest.TestCase):

    def test_integrate_float32(self):
        ass3 = Assignment3()
        f1 = np.poly1d([-1, 0, 1])
        r = ass3.integrate(f1, -1, 1, 10)
        self.assertEqual(r.dtype, np.float32)

    def test_integrate_hard_case(self):
        ass3 = Assignment3()
        f1 = strong_oscilations()
        r = ass3.integrate(f1, 0.09, 10, 20)
        true_result = -7.78662 * 10 ** 33
        self.assertGreaterEqual(0.001, abs((r - true_result) / true_result))


if __name__ == "__main__":
    unittest.main()
