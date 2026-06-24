from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


# Crear restaurante
restaurante = Restaurante()

# Crear productos
producto1 = Producto("Maito de Tilapia completo", 5.50, "Plato Principal", True)
producto2 = Producto("Batido de Durazno y Guayusa", 3.25, "Bebida", True)

# Crear clientes
cliente1 = Cliente("Clide Alva", 18, "clide@gmail.com", True)
cliente2 = Cliente("María López", 30, "maria@gmail.com", False)

# Agregar productos
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)

# Agregar clientes
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
print("====================================================")
print(" SISTEMA DE GESTIÓN DEL RESTAURANTE EL BAMBÚ COTUNDO")
print("====================================================")

restaurante.mostrar_productos()
restaurante.mostrar_clientes()