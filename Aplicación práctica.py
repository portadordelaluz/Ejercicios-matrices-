print("\nAPLICACIÓN PRÁCTICA:\n")

# Ejemplo: ventas de 3 productos en 3 meses
ventas = np.array([
    [100, 120, 130],
    [80, 90, 100],
    [150, 160, 170]
])

# Precio por producto
precios = np.array([10, 20, 15])

# Ingresos por mes
ingresos = ventas * precios.reshape(3,1)

print("Ventas:\n", ventas)
print("Ingresos:\n", ingresos)
print("Ingreso total por producto:", ingresos.sum(axis=1))
