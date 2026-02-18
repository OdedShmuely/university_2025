"""
In this assignment you should fit a model function of your choice to data
that you sample from a contour of given shape. Then you should calculate
the area of that shape.

The sampled data is very noisy so you should minimize the mean least squares
between the model you fit and the data points you sample.

During the testing of this assignment running time will be constrained. You
receive the maximal running time as an argument for the fitting method. You
must make sure that the fitting function returns at most 5 seconds after the
allowed running time elapses. If you know that your iterations may take more
than 1-2 seconds break out of any optimization loops you have ahead of time.

Note: You are allowed to use any numeric optimization libraries and tools you want
for solving this assignment.
Note: !!!Despite previous note, using reflection to check for the parameters
of the sampled function is considered cheating!!! You are only allowed to
get (x,y) points from the given shape by calling sample().
"""

import numpy as np
import time
import random
from functionUtils import AbstractShape


class Assignment5:
    def __init__(self):
        pass

    def area(self, contour, maxerr=0.001):
        """
        Computes the area using Richardson Extrapolation.
        """
        def shoelace(pts):
            pts = np.array(pts)
            x, y = pts[:, 0], pts[:, 1]
            return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))

        n = 64
        points_n = contour(n)
        area_n = shoelace(points_n)

        for _ in range(10):
            points_2n = contour(2 * n)
            area_2n = shoelace(points_2n)
            # Richardson Extrapolation
            extrapolated_area = area_2n + (area_2n - area_n) / 3.0
            if np.abs(area_2n - area_n) < maxerr:
                return np.float32(extrapolated_area)

            area_n = area_2n
            n *= 2
            if n > 10000: break
        return np.float32(area_n)

    def fit_shape(self, sample, maxtime):
        """
        Circle (Robust) or Fourier (General).
        """
        start_time = time.time()
        samples = []
        max_points = 4096
        time_limit = maxtime * 0.9

        while (time.time() - start_time) < time_limit:
            try:
                samples.append(sample())
                if len(samples) >= max_points:
                    break
            except:
                break
        if not samples:
            return MyShape(method='fourier', points=np.empty((0, 2)))
        points = np.array(samples)
        points = points[np.isfinite(points).all(axis=1)]

        if len(points) < 10:
            return MyShape(method='fourier', points=points)
        centroid = np.mean(points, axis=0)
        dists = np.linalg.norm(points - centroid, axis=1)
        mean_dist = np.mean(dists)
        std_dist = np.std(dists)
        cv = std_dist / mean_dist if mean_dist > 1e-6 else 0

        if cv < 0.20:
            radius = np.median(dists)
            return MyShape(method='circle', center=centroid, radius=radius)
        else:
            return MyShape(method='fourier', points=points)


class MyShape(AbstractShape):
    def __init__(self, method='fourier', center=None, radius=None, points=None):
        self.method = method
        if method == 'circle':
            self.center = center
            self.radius = radius

        elif method == 'fourier':
            self._fit_fourier(points)

    def _fit_fourier(self, points):
        if len(points) == 0:
            self.Z_trunc = np.array([0])
            self.fourier_N = 1
            return
        centroid = np.mean(points, axis=0)
        angles = np.arctan2(points[:, 1] - centroid[1], points[:, 0] - centroid[0])
        sort_idx = np.argsort(angles)
        points_sorted = points[sort_idx]
        diffs = np.diff(points_sorted, axis=0, prepend=points_sorted[-1:])
        dists = np.linalg.norm(diffs, axis=1)
        cum_dist = np.cumsum(dists)
        total_len = cum_dist[-1]

        if total_len < 1e-6:
            self.Z_trunc = np.array([complex(centroid[0], centroid[1])])
            self.fourier_N = 1
            return

        n_target = 1024
        new_dists = np.linspace(0, total_len, n_target, endpoint=False)
        new_x = np.interp(new_dists, cum_dist, points_sorted[:, 0])
        new_y = np.interp(new_dists, cum_dist, points_sorted[:, 1])

        z = new_x + 1j * new_y
        Z = np.fft.fft(z)

        n_harmonics = 20
        self.Z_trunc = np.zeros_like(Z)
        self.Z_trunc[0] = Z[0]
        self.Z_trunc[1:n_harmonics + 1] = Z[1:n_harmonics + 1]
        self.Z_trunc[-n_harmonics:] = Z[-n_harmonics:]
        self.fourier_N = n_target

    def contour(self, n):
        if self.method == 'circle':
            theta = np.linspace(0, 2 * np.pi, n, endpoint=False)
            x = self.center[0] + self.radius * np.cos(theta)
            y = self.center[1] + self.radius * np.sin(theta)
            return np.column_stack([x, y])

        elif self.method == 'fourier':
            Z_new = np.zeros(n, dtype=complex)
            limit = min(len(self.Z_trunc) // 2, n // 2 - 1)
            Z_new[0] = self.Z_trunc[0]
            Z_new[1:limit + 1] = self.Z_trunc[1:limit + 1]
            Z_new[-limit:] = self.Z_trunc[-limit:]
            Z_new *= (n / self.fourier_N)
            z_recon = np.fft.ifft(Z_new)

            return np.column_stack([z_recon.real, z_recon.imag])

    def area(self):
        if self.method == 'circle':
            return np.float32(np.pi * (self.radius ** 2))
        elif self.method == 'fourier':
            pts = self.contour(2048)
            x, y = pts[:, 0], pts[:, 1]
            a = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
            return np.float32(a)