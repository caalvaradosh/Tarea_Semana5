class Cliente:
    """Representa un cliente registrado."""

    def __init__(self, nombre: str, edad: int, correo: str, cliente_frecuente: bool):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.cliente_frecuente = cliente_frecuente

    def __str__(self):
        tipo = "Frecuente" if self.cliente_frecuente else "Nuevo"
        return f"{self.nombre} | {self.edad} años | {self.correo} | {tipo}"