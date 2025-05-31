import numpy as np
from scipy.optimize import fsolve

zeta = 0.5

def eqs(v):
    wn, k, p = v
    re = -zeta * wn
    im = wn * np.sqrt(1 - zeta**2)
    s1 = complex(re, im)
    s2 = complex(re, -im)
    a = -2 * re
    b = abs(s1)**2
    e1 = a - p - 9
    e2 = b - a * p - 18
    e3 = -b * p - k
    return [e1, e2, e3]

sol = fsolve(eqs, (1, 10, -1))
wn, k, p = sol

Kv = k / (3 * 6)
ess = 1 / Kv

print("k =", round(k, 4))

print("Kv =", round(Kv, 4))

print("ess =", round(ess, 4))

#Question4