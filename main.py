import sympy as sym

u = sym.symbols('u')

print(sym.integrate(pow(6 - 2*u,2),u))