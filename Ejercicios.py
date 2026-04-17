import numpy as np

# =========================
# 5 EJERCICIOS DE SUMA (3x3)
# =========================
print("SUMAS:\n")

A1 = np.array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])

B1 = np.array([[9, 8, 7],
               [6, 5, 4],
               [3, 2, 1]])

print("1:\n", A1 + B1)

A2 = np.array([[2, 0, 1],
               [3, 5, 7],
               [1, 2, 4]])

B2 = np.array([[1, 1, 1],
               [2, 2, 2],
               [3, 3, 3]])

print("2:\n", A2 + B2)

A3 = np.array([[0, 1, 2],
               [3, 4, 5],
               [6, 7, 8]])

B3 = np.array([[8, 7, 6],
               [5, 4, 3],
               [2, 1, 0]])

print("3:\n", A3 + B3)

A4 = np.array([[4, 5, 6],
               [7, 8, 9],
               [1, 2, 3]])

B4 = np.array([[3, 3, 3],
               [2, 2, 2],
               [1, 1, 1]])

print("4:\n", A4 + B4)

A5 = np.array([[9, 8, 7],
               [6, 5, 4],
               [3, 2, 1]])

B5 = np.array([[1, 0, 1],
               [0, 1, 0],
               [1, 0, 1]])

print("5:\n", A5 + B5)


# =========================
# 5 EJERCICIOS DE RESTA (3x3)
# =========================
print("\nRESTAS:\n")

print("1:\n", A1 - B1)
print("2:\n", A2 - B2)
print("3:\n", A3 - B3)
print("4:\n", A4 - B4)
print("5:\n", A5 - B5)


# =========================
# 5 PRODUCTOS POR ESCALAR (3x3)
# =========================
print("\nPRODUCTO POR ESCALAR:\n")

print("1:\n", 2 * A1)
print("2:\n", -1 * A2)
print("3:\n", 3 * A3)
print("4:\n", 4 * A4)
print("5:\n", 5 * A5)

