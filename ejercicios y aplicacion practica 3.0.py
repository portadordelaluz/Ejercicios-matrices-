# ============================================================
# ECUACIONES PARAMETRICAS Y PLANOS
# ============================================================
# Trabajo de Geometria Analitica en Python
#
# Temas:
# 1. Ecuaciones parametricas
# 2. Ecuacion cartesiana del plano
# 3. Interseccion entre recta y plano
# 4. Aplicacion practica
#
# Bibliotecas utilizadas:
# - NumPy
# - SymPy
# - Matplotlib
# ============================================================

# ============================================================
# IMPORTACION DE BIBLIOTECAS
# ============================================================

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# ============================================================
# 1. ECUACIONES PARAMETRICAS
# ============================================================

print("\n================================================")
print("1. ECUACIONES PARAMETRICAS")
print("================================================")

# ------------------------------------------------------------
# EJERCICIO 1
# ------------------------------------------------------------

print("\nEJERCICIO 1")

# Punto de la recta
P1 = np.array([1, 2, 3])

# Vector direccion
D1 = np.array([2, -1, 4])

print("Punto:", P1)
print("Direccion:", D1)

print("Ecuaciones parametricas:")
print("x = 1 + 2t")
print("y = 2 - t")
print("z = 3 + 4t")

# ------------------------------------------------------------
# EJERCICIO 2
# ------------------------------------------------------------

print("\nEJERCICIO 2")

P2 = np.array([0, 1, -2])
D2 = np.array([3, 5, 1])

print("Punto:", P2)
print("Direccion:", D2)

print("x = 3t")
print("y = 1 + 5t")
print("z = -2 + t")

# ------------------------------------------------------------
# EJERCICIO 3
# ------------------------------------------------------------

print("\nEJERCICIO 3")

P3 = np.array([2, -1, 0])
D3 = np.array([1, 4, -3])

print("Punto:", P3)
print("Direccion:", D3)

print("x = 2 + t")
print("y = -1 + 4t")
print("z = -3t")

# ------------------------------------------------------------
# EJERCICIO 4
# ------------------------------------------------------------

print("\nEJERCICIO 4")

P4 = np.array([-2, 3, 1])
D4 = np.array([5, -2, 6])

print("Punto:", P4)
print("Direccion:", D4)

print("x = -2 + 5t")
print("y = 3 - 2t")
print("z = 1 + 6t")

# ------------------------------------------------------------
# EJERCICIO 5
# ------------------------------------------------------------

print("\nEJERCICIO 5")

P5 = np.array([4, 0, -1])
D5 = np.array([-3, 2, 5])

print("Punto:", P5)
print("Direccion:", D5)

print("x = 4 - 3t")
print("y = 2t")
print("z = -1 + 5t")

# ============================================================
# 2. ECUACION CARTESIANA DEL PLANO
# ============================================================

print("\n================================================")
print("2. ECUACION CARTESIANA DEL PLANO")
print("================================================")

# ------------------------------------------------------------
# PUNTOS A
# ------------------------------------------------------------

print("\nPUNTOS A")

# Definicion de puntos
P = sp.Point(1, -2, 3)
Q = sp.Point(4, 6, 1)
R = sp.Point(-2, 1, 1)

# Creacion del plano
plano_A = sp.Plane(P, Q, R)

print("Punto P:", P)
print("Punto Q:", Q)
print("Punto R:", R)

# Mostrar ecuacion del plano
print("Ecuacion del plano:")
print(plano_A.equation())

# ------------------------------------------------------------
# PUNTOS B
# ------------------------------------------------------------

print("\nPUNTOS B")

S = sp.Point(1, -1, 1)
T = sp.Point(2, 3, 5)
U = sp.Point(6, -4, 3)

plano_B = sp.Plane(S, T, U)

print("Punto S:", S)
print("Punto T:", T)
print("Punto U:", U)

print("Ecuacion del plano:")
print(plano_B.equation())

# ============================================================
# 3. INTERSECCION ENTRE RECTA Y PLANO
# ============================================================

print("\n================================================")
print("3. INTERSECCION ENTRE RECTA Y PLANO")
print("================================================")

# Variable simbolica
t = sp.symbols('t')

# Punto P
P = np.array([1, -1, 2])

# Vector direccion N
N = np.array([1, 2, 3])

print("\nPunto P:", P)
print("Direccion N:", N)

# Ecuaciones parametricas de la recta
x = 1 + t
y = -1 + 2*t
z = 2 + 3*t

print("\nRecta:")
print("x = 1 + t")
print("y = -1 + 2t")
print("z = 2 + 3t")

# Plano perpendicular a N
# x + 2y + 3z - 2 = 0

print("\nPlano:")
print("x + 2y + 3z - 2 = 0")

# Sustitucion en el plano
ecuacion = x + 2*y + 3*z - 2

# Resolver valor de t
valor_t = sp.solve(ecuacion, t)

print("\nValor de t:")
print(valor_t)

# Calculo del punto de interseccion
t_inter = valor_t[0]

x_inter = x.subs(t, t_inter)
y_inter = y.subs(t, t_inter)
z_inter = z.subs(t, t_inter)

print("\nPunto de interseccion:")
print("(", x_inter, ",", y_inter, ",", z_inter, ")")

# ============================================================
# 4. APLICACION PRACTICA
# ============================================================

print("\n================================================")
print("4. APLICACION PRACTICA")
print("================================================")

# Problema:
# Trayectoria de un avion en el espacio

# Punto inicial
P0 = np.array([0, 0, 0])

# Direccion del avion
direccion = np.array([2, 3, 4])

print("\nPunto inicial:", P0)
print("Direccion:", direccion)

# Parametro
t = np.linspace(0, 5, 100)

# Coordenadas de la trayectoria
x = P0[0] + direccion[0] * t
y = P0[1] + direccion[1] * t
z = P0[2] + direccion[2] * t

# ============================================================
# GRAFICA 3D
# ============================================================

# Crear figura
fig = plt.figure()

# Crear espacio 3D
ax = fig.add_subplot(111, projection='3d')

# Dibujar trayectoria
ax.plot(x, y, z, label='Trayectoria del avion')

# Etiquetas
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

# Titulo
plt.title("Aplicacion de Ecuaciones del Plano")

# Leyenda
ax.legend()

# Mostrar grafica
plt.show()