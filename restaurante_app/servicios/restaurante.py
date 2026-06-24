from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Administra los productos y clientes."""

    def __init__(self):
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    def mostrar_productos(self):
        print("\n========== PRODUCTOS ==========")

        for producto in self.productos:
            print(producto)

    def mostrar_clientes(self):
        print("\n========== CLIENTES ==========")

        for cliente in self.clientes:
            print(cliente)