def eval_quadratic(a, b, c, x):
    q = a*(x**2) + b*x + c
    return q

def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    k = eval_quadratic(a1, b1, c1, x1)
    j = eval_quadratic(a2, b2, c2, x2)
    return (k + j)

print(two_quadratics(1, 1, 1, 1, 1, 1 ,1 ,1))