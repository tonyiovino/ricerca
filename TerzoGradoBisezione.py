basso = 0.3
alto = 0.75

count = 0

passo = 0.001
zero = 0.00001

while basso < alto:
    print("\nCount:", count)
    print("Cerca tra", basso, "e", alto) 

    x = (basso+alto) / 2.

    polinomio = x**3 + 4.5 * x**2 + 3.5 * x - 3
    polinomio_b = basso**3 + 4.5 * basso**2 + 3.5 * basso - 3
    polinomio_a = alto**3 + 4.5 * alto**2 + 3.5 * alto - 3

    print("Da testare:", x)

    if abs(polinomio) < zero:
        break

    elif polinomio * polinomio_a > 0:
        alto = x

    else:
        basso = x

    count += 1

print("\nSoluzione: ", x)
print("Trovata in", count, "passaggi")