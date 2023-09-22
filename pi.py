import decimal

decimal.getcontext().prec = 1000

a = decimal.Decimal(1)
b = decimal.Decimal(1) / decimal.Decimal(2).sqrt()
t = decimal.Decimal(1) / decimal.Decimal(4)
p = decimal.Decimal(1)

while True:
    a_new = (a + b) / 2
    b_new = (a * b).sqrt()
    t_new = t - p * (a - a_new) ** 2
    p_new = 2 * p

    pi = (a_new + b_new) ** 2 / (4 * t_new)

    print(pi)

    a = a_new
    b = b_new
    t = t_new
    p = p_new
