# ============================================================
# TRABAJO DE VECTORES EN PYTHON
# ============================================================
# Temas:
# 1. Vectores paralelos
# 2. Vectores perpendiculares
# 3. Módulo de un vector
# 4. Ángulo entre dos vectores
# 5. Aplicación práctica de vectores
#
# Bibliotecas utilizadas:
# - NumPy
# - Matplotlib
# ============================================================

# Importación de bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. VECTORES PARALELOS
# ============================================================

print("\n==============================")
print("1. VECTORES PARALELOS")
print("==============================")

# ------------------------------------------------------------
# Ejercicio 1
# ------------------------------------------------------------

# Definición de vectores
A = np.array([2, 4, 6])
B = np.array([1, 2, 3])

# División entre componentes
razones = A / B

print("\nEjercicio 1")
print("Vector A:", A)
print("Vector B:", B)

# Verificación de paralelismo
if np.all(razones == razones[0]):
    print("Los vectores son paralelos")
else:
    print("Los vectores no son paralelos")

# ------------------------------------------------------------
# Ejercicio 2
# ------------------------------------------------------------

C = np.array([3, -6, 9])
D = np.array([-1, 2, -3])

razones = C / D

print("\nEjercicio 2")
print("Vector C:", C)
print("Vector D:", D)

if np.all(razones == razones[0]):
    print("Los vectores son paralelos")
else:
    print("Los vectores no son paralelos")

# ------------------------------------------------------------
# Ejercicio 3
# ------------------------------------------------------------

E = np.array([4, 2, 8])
F = np.array([2, 1, 5])

razones = E / F

print("\nEjercicio 3")
print("Vector E:", E)
print("Vector F:", F)

if np.all(razones == razones[0]):
    print("Los vectores son paralelos")
else:
    print("Los vectores no son paralelos")


# ============================================================
# 2. VECTORES PERPENDICULARES
# ============================================================

print("\n==============================")
print("2. VECTORES PERPENDICULARES")
print("==============================")

# ------------------------------------------------------------
# Ejercicio 1
# ------------------------------------------------------------

A = np.array([2, 3])
B = np.array([3, -2])

# Producto punto
producto = np.dot(A, B)

print("\nEjercicio 1")
print("Producto punto:", producto)

# Si el producto punto es 0, son perpendiculares
if producto == 0:
    print("Los vectores son perpendiculares")
else:
    print("Los vectores no son perpendiculares")

# ------------------------------------------------------------
# Ejercicio 2
# ------------------------------------------------------------

C = np.array([1, 2, 3])
D = np.array([4, -8, 4])

producto = np.dot(C, D)

print("\nEjercicio 2")
print("Producto punto:", producto)

if producto == 0:
    print("Los vectores son perpendiculares")
else:
    print("Los vectores no son perpendiculares")

# ------------------------------------------------------------
# Ejercicio 3
# ------------------------------------------------------------

E = np.array([5, 1])
F = np.array([2, 3])

producto = np.dot(E, F)

print("\nEjercicio 3")
print("Producto punto:", producto)

if producto == 0:
    print("Los vectores son perpendiculares")
else:
    print("Los vectores no son perpendiculares")


# ============================================================
# 3. MÓDULO DE UN VECTOR
# ============================================================

print("\n==============================")
print("3. MÓDULO DE UN VECTOR")
print("==============================")

# ------------------------------------------------------------
# Ejercicio 1
# ------------------------------------------------------------

A = np.array([3, 4])

# Cálculo del módulo
modulo = np.linalg.norm(A)

print("\nEjercicio 1")
print("Vector:", A)
print("Módulo:", modulo)

# ------------------------------------------------------------
# Ejercicio 2
# ------------------------------------------------------------

B = np.array([2, -3, 6])

modulo = np.linalg.norm(B)

print("\nEjercicio 2")
print("Vector:", B)
print("Módulo:", modulo)

# ------------------------------------------------------------
# Ejercicio 3
# ------------------------------------------------------------

C = np.array([-1, 5, 2])

modulo = np.linalg.norm(C)

print("\nEjercicio 3")
print("Vector:", C)
print("Módulo:", modulo)


# ============================================================
# 4. ÁNGULO ENTRE DOS VECTORES
# ============================================================

print("\n==============================")
print("4. ÁNGULO ENTRE DOS VECTORES")
print("==============================")

# ------------------------------------------------------------
# Ejercicio 1
# ------------------------------------------------------------

A = np.array([1, 0])
B = np.array([0, 1])

# Producto punto
producto = np.dot(A, B)

# Módulos
modA = np.linalg.norm(A)
modB = np.linalg.norm(B)

# Fórmula del ángulo
angulo = np.degrees(np.arccos(producto / (modA * modB)))

print("\nEjercicio 1")
print("Ángulo:", angulo, "grados")

# ------------------------------------------------------------
# Ejercicio 2
# ------------------------------------------------------------

C = np.array([1, 1])
D = np.array([1, 0])

producto = np.dot(C, D)

modC = np.linalg.norm(C)
modD = np.linalg.norm(D)

angulo = np.degrees(np.arccos(producto / (modC * modD)))

print("\nEjercicio 2")
print("Ángulo:", angulo, "grados")

# ------------------------------------------------------------
# Ejercicio 3
# ------------------------------------------------------------

E = np.array([2, 1])
F = np.array([-1, 2])

producto = np.dot(E, F)

modE = np.linalg.norm(E)
modF = np.linalg.norm(F)

angulo = np.degrees(np.arccos(producto / (modE * modF)))

print("\nEjercicio 3")
print("Ángulo:", angulo, "grados")


# ============================================================
# 5. APLICACIÓN PRÁCTICA DE VECTORES
# ============================================================

print("\n==============================")
print("5. APLICACIÓN PRÁCTICA")
print("==============================")

# Problema:
# Un dron se desplaza:
# - 4 km hacia el este
# - 3 km hacia el norte

# Vector horizontal
v1 = np.array([4, 0])

# Vector vertical
v2 = np.array([0, 3])

# ------------------------------------------------------------
# Suma de vectores
# ------------------------------------------------------------

resultado = v1 + v2

# ------------------------------------------------------------
# Cálculo del módulo
# ------------------------------------------------------------

modulo = np.linalg.norm(resultado)

# ------------------------------------------------------------
# Cálculo del ángulo
# ------------------------------------------------------------

angulo = np.degrees(np.arctan2(resultado[1], resultado[0]))

# ------------------------------------------------------------
# Resultados
# ------------------------------------------------------------

print("\nVector 1:", v1)
print("Vector 2:", v2)
print("Vector resultante:", resultado)
print("Distancia recorrida:", modulo)
print("Ángulo:", angulo, "grados")

# ============================================================
# GRÁFICA DE LOS VECTORES
# ============================================================

# Vector 1
plt.quiver(
    0, 0,
    v1[0], v1[1],
    angles='xy',
    scale_units='xy',
    scale=1,
    label='Vector Este'
)

# Vector 2
plt.quiver(
    0, 0,
    v2[0], v2[1],
    angles='xy',
    scale_units='xy',
    scale=1,
    label='Vector Norte'
)

# Vector resultante
plt.quiver(
    0, 0,
    resultado[0], resultado[1],
    angles='xy',
    scale_units='xy',
    scale=1,
    label='Vector Resultante'
)

# Límites de la gráfica
plt.xlim(0, 6)
plt.ylim(0, 6)

# Cuadrícula
plt.grid()

# Etiquetas
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Título
plt.title("Aplicación Práctica de Vectores")

# Leyenda
plt.legend()

# Mostrar gráfica
plt.show()