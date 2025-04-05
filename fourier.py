import math
import numpy as np


class Function:
    def __init__(self, T, X):
        self.T = list(sorted(T))
        self.X = X
        assert len(set(self.T)) == len(self.T)
        assert min(self.T) >= 0 and max(self.T) <= 1

    def __mul__(self, other):
        newT = list(set(self.T + other.T))
        newX = {}

        for t in newT:
            newX[t] = self(t) * other(t)
        
        return Function(newT, newX)

    def integrate(self):
        res = 0
        for i in range(len(self.T) - 1):
            res += self.X[self.T[i]] * (self.T[i + 1] - self.T[i])
        return res

    def __call__(self, t):
        assert 0 <= t and t <= 1
        left, right = 0, len(self.T) - 1
        
        while left < right:
            mid = (left + right) // 2
            if self.T[mid] < t:
                left = mid + 1
            else:
                right = mid
        
        return self.X[self.T[left]]
        




class FourierComposition:
    def __init__(self, N = 51):
        assert N % 2 == 1
        self.N = N
        self.coef = [0j] * self.N

    def fit(self, f: Function):
        self.f = f

        for i in range(0, self.N):
            self.coef[i] = (self.f * Function(self.f.T, {t: math.e ** (1j * (self.N // 2 - i) * t) for t in self.f.T})).integrate() / math.sqrt(2 * math.pi)

    def __call__(self, t):
        res = 0
        for i, c in enumerate(self.coef):
            res += c * math.e ** (1j * (i - self.N // 2) * t) / math.sqrt(2 * math.pi)
        return res