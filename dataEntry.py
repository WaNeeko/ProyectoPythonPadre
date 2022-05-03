def formulario():
    class Producto:
        def __init__(self):
            self.precio = None
            self.cantidad = None
    class Pedido:
        def __init__(self):
            self.teVerde = Producto()
            self.teNegro = Producto()
            self.mielAlgarrobo = Producto()
    class Cliente:
        def __init__(self):
            self.DNI = None
            self.correo = None
    class Formulario:
        def __init__(self):
            self.fecha = None
            self.pedido = Pedido()
            self.cliente = Cliente()
    return Formulario()

formulario()