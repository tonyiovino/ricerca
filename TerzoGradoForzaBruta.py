print("Terzo Grado\n")

print("Data l'equazione x^3 + 4.5 x^2 + 3.5 x - 3 = 0\n")

print("Trova la soluzione compresa nell'intervallo (0.3, 0.75), mediante metodo a forza bruta.\n")

x = 0.3

xf = 0.75

passo = 0.001

zero = 0.00001

while x <= xf:
    polinomio = abs(x**3 + 4.5 * x**2 + 3.5 * x - 3)
    if polinomio < zero:
        break
    x = x + passo
    print("Polinomio: ", polinomio)
print("X: ", x)