from mpi4py import MPI
import numpy as np
import matplotlib.pyplot as plt

comm = MPI.COMM_WORLD
my_rank = comm.Get_rank()
size = comm.Get_size() 

def funcion(x):
    fxi = np.sqrt(x)*np.sin(x)
    return(fxi)
def integral(A,B,N,h):
    integral = (funcion(A) + funcion(B))/2.0
    x = A
    for i in range(1,int(N)):
        x = x + h
        integral = integral + funcion(x)
        i=integral*h
    return i
 
a = 1
b = 10
tramos=100
dest=0
total=0
integral_suma=0.0

h = (b-a)/tramos 
N = tramos/size 

A = a + my_rank*N*h
B = a + N*h

valor=integral(A,B,N,h)

if my_rank == 0:
    total = valor
    for source in range(1,size):
        valor = comm.recv(source=source)
        print(my_rank,":",source," ",valor,"\n")
        total = total + valor
else :
    print(my_rank,":",dest," ",valor,"\n")
    comm.send(valor, dest=0)

if (my_rank == 0):
    print("n=",tramos,"  \n")
    print("integral de ",a,"a ",b,"=",total,"\n")
    

muestras = tramos + 1
xi = np.linspace(a, b, muestras)
fi = funcion(xi)
    
xig = np.linspace(a, b, muestras * 10)
fig = funcion(xig)
plt.plot(xig, fig)
plt.fill_between(xi, 0, fi, color = 'y')
plt.title('Integral: Regla de Trapecios')
for i in range(0, muestras, 1):
    plt.axvline(xi[i], color = 'w')
plt.plot(xi, fi, 'o')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.savefig("Grafica.jpg")