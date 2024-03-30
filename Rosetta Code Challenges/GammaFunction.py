# Gamme function
import numpy as np
def gamma_function(x, num_points=100):
    xi, wi = np.polynomial.legendre.leggauss(num_points)
    t = (xi + 1) / 2
    integrand = t**(x - 1) * np.exp(-t)
    integral = np.sum(integrand * wi) * 0.5
    return integral
x = 3.5
result = gamma_function(x)
print(" Γ({}) ≈ {:.8f}".format(x, result))