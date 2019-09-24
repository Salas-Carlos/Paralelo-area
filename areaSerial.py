import numpy as np
import matplotlib.pyplot as plt

functionx = lambda x : np.cos(x) + x**3

def integral(a, b, tramos):
    h = (b - a) / tramos
    x = a
    suma = functionx(x)
    for i in range(0, tramos - 1, 1):
        x = x + h
        suma = suma + 2 * functionx(x)
    suma = suma + functionx(b)
    area = h * (suma / 2)
    return area

a = 1
b = 10
tramos = 100

print(integral(a, b, tramos))

for i in range(1, tramos):
    print("tramos ", i, "area ", integral(a, b, i))


muestras = tramos + 1
xi = np.linspace(a, b, muestras)
fi = functionx(xi)

# Gráfica
# Referencia función contínua
xig = np.linspace(a, b, muestras * 10)
fig = functionx(xig)
plt.plot(xig, fig)
# Trapecios
plt.fill_between(xi, 0, fi, color = 'y')
plt.title('Integral: Regla de Trapecios')
for i in range(0, muestras, 1):
    plt.axvline(xi[i], color = 'w')
plt.plot(xi, fi, 'o') # puntos muestra
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

print('tramos: ', tramos)
print('Integral: ', area)