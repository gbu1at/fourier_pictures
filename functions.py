from fourier import * 
from setting import *



def get_function(file_name):
    with open(file_name, "r") as f:
        data = list(map(int, f.read().split()))

        X, Y = list(map(lambda t : (t - WIDTH / 2) * XMAX / WIDTH * 2, data[::2])), list(map(lambda t : (t - HEIGHT / 2) * YMAX / HEIGHT * 2, data[1::2]))

        cntp = len(data) // 2

        sum_len = 0

        T = [None] * cntp
        CX = {}

        for i in range(cntp - 1):
            sum_len += math.sqrt((X[i] - X[i + 1]) ** 2 + (Y[i] - Y[i + 1]) ** 2)
        
        T[0] = 0
        CX[0] = X[0] + 1j * Y[0]

        pref_sum_len = 0

        for i in range(1, cntp):
            pref_sum_len += math.sqrt((X[i] - X[i - 1]) ** 2 + (Y[i] - Y[i - 1]) ** 2)
            T[i] = pref_sum_len / sum_len
            CX[T[i]] = X[i] + 1j * Y[i]

        return Function(T, CX)
