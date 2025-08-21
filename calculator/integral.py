import math
from scipy import integrate

def f(x):
    return math.sin(x)

integral, error = integrate.quad(f, -1, 1)

print(integral)
