x = 0.3

basso = x
alto = 0.75

count = 0

passo = 0.001
zero = 0.00001

while basso <= alto:
    print("\nCount:", count)
    print("Cerca tra", basso, "e", alto)

    x = (basso+alto) / 2.
    polinomio = abs(x**3 + 4.5 * x**2 + 3.5 * x - 3)

    print("Da testare:", x)

    if polinomio == zero:
        break

    elif polinomio < zero:
        basso = x + passo

    else:
        alto = x - passo

    count += 1

print("\nSoluzione:", x)
print("Trovata in", count, "passaggi")