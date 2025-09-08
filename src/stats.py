import numpy as np

def mean(values):
    arr = np.array(values, dtype=float)
    return float(np.mean(arr))

def fib(n):
    if n < 0:
        raise ValueError("n debe ser no negativo")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
