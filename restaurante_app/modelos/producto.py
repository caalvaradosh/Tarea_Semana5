class Producto:
    """Representa un producto disponible en el restaurante."""

    def __init__(self, nombre: str, precio: float, categoria: str, disponible: bool):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.nombre} | {self.categoria} | ${self.precio:.2f} | {estado}"