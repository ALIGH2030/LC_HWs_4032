import sympy as sp

K = sp.Symbol('K', real=True)
s = sp.Symbol('s')

eq = s**3 + 18*s**2 + 77*s + K

a3 = 1
a2 = 18
a1 = 77
a0 = K

r1 = (a2*a1 - a3*a0)/a2

kritik_k = sp.solve(r1, K)[0]
range_stable = sp.solve(r1 > 0, K)

print("پایداری: 0 < K <", int(kritik_k))
print("پایداری بحرانی: K =", int(kritik_k))
print("ناپایداری: K <=", 0, "یا K >", int(kritik_k))

#سوال2